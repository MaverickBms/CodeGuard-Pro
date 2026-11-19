/* Motor del Mundo CodeGuard: exploración 2D, diálogos, misiones y guardado. */
(function () {
  'use strict';

  const Model = window.CodeGuardMundoModel;
  const World = window.CodeGuardMundoWorld;
  const Sprites = window.CodeGuardMundoSprites;
  const configNode = document.getElementById('mundo-config');
  if (!Model || !World || !Sprites || !configNode) return;

  const canvas = document.getElementById('mundoCanvas');
  const ctx = canvas ? canvas.getContext('2d') : null;
  if (!canvas || !ctx) return;

  const dom = {
    carga: document.getElementById('mundoCarga'),
    error: document.getElementById('mundoError'),
    errorTexto: document.getElementById('mundoErrorTexto'),
    dialogo: document.getElementById('mundoDialogo'),
    dialogoNombre: document.getElementById('mundoDialogoNombre'),
    dialogoTexto: document.getElementById('mundoDialogoTexto'),
    dialogoAccion: document.getElementById('btnMundoDialogoAccion'),
    pausa: document.getElementById('mundoPausa'),
    minijuego: document.getElementById('mundoMinijuego'),
    formMinijuego: document.getElementById('mundoFormMinijuego'),
    minijuegoError: document.getElementById('mundoMinijuegoError'),
    misiones: document.getElementById('mundoMisiones'),
    inventario: document.getElementById('mundoInventario'),
    nivel: document.getElementById('hudNivel'),
    xp: document.getElementById('hudXp'),
    misionesHud: document.getElementById('hudMisiones'),
    audio: document.getElementById('btnMundoAudio'),
    guardado: document.getElementById('mundoEstadoGuardado'),
    academicoTexto: document.getElementById('mundoAcademicoTexto'),
    academicoEnlace: document.getElementById('mundoAcademicoEnlace')
  };

  let running = true;
  let config;
  try {
    config = JSON.parse(configNode.textContent);
  } catch (error) {
    showFatal('La configuración del mundo no es válida.');
    return;
  }

  const map = World.world;
  const state = {
    misiones: config.misiones || [],
    banderas: config.banderas || {},
    inventario: config.inventario || [],
    experiencia: config.experiencia || 0,
    nivel: config.nivel || 1,
    xpSiguiente: config.xp_siguiente || 50,
    tiempoJugado: config.tiempo_jugado || 0,
    audioSilenciado: Boolean(config.audio_silenciado),
    puedeGuardar: document.getElementById('mundoShell').dataset.puedeGuardar === '1'
  };
  const player = {
    x: Number(config.posicion && config.posicion.x) + 0.5,
    y: Number(config.posicion && config.posicion.y) + 0.5,
    direction: (config.posicion && config.posicion.direccion) || 'down',
    moving: false,
    frame: 0
  };
  if (!Number.isFinite(player.x) || !Number.isFinite(player.y)) {
    player.x = map.spawn.x + 0.5;
    player.y = map.spawn.y + 0.5;
  }

  const VIEW_W = canvas.width / Sprites.T;
  const VIEW_H = canvas.height / Sprites.T;
  const keys = new Set();
  const pointers = new Set();
  let paused = false;
  let modalOpen = false;
  let lastTime = 0;
  let elapsed = 0;
  let saveTimer = null;
  let saving = false;
  let audioContext = null;
  let activeQuest = null;
  let dialogueAction = null;

  ctx.imageSmoothingEnabled = false;
  dom.carga.hidden = true;
  dom.error.hidden = true;
  canvas.focus();

  function setStatus(texto) {
    if (dom.guardado) dom.guardado.textContent = texto;
  }

  function showFatal(message) {
    if (dom.carga) dom.carga.hidden = true;
    if (dom.error) {
      dom.error.hidden = false;
      if (dom.errorTexto) dom.errorTexto.textContent = message;
    }
    running = false;
    if (dom.guardado) dom.guardado.textContent = message;
  }

  function csrfToken() {
    const input = document.querySelector('#mundoCsrf input[name="csrfmiddlewaretoken"]');
    return input ? input.value : '';
  }

  async function api(url, payload) {
    const response = await fetch(url, {
      method: 'POST',
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken()
      },
      body: JSON.stringify(payload)
    });
    let data = null;
    try {
      data = await response.json();
    } catch (error) {
      data = { error: 'El servidor devolvió una respuesta no válida.' };
    }
    if (!response.ok) {
      throw new Error((data && data.error) || `Error HTTP ${response.status}`);
    }
    return data;
  }

  function applyServerState(nuevo) {
    if (!nuevo) return;
    state.misiones = nuevo.misiones || state.misiones;
    state.banderas = nuevo.banderas || state.banderas;
    state.inventario = nuevo.inventario || state.inventario;
    state.experiencia = nuevo.experiencia || 0;
    state.nivel = nuevo.nivel || 1;
    state.xpSiguiente = nuevo.xp_siguiente || 50;
    state.tiempoJugado = nuevo.tiempo_jugado || state.tiempoJugado;
    state.audioSilenciado = Boolean(nuevo.audio_silenciado);
    renderHud();
    renderSidebar();
  }

  function comandoMision(id) {
    return state.misiones.find((mision) => mision.id === id) || null;
  }

  function renderHud() {
    const completadas = state.misiones.filter((m) => m.estado === 'completada').length;
    dom.nivel.textContent = `Nivel ${state.nivel}`;
    dom.xp.textContent = `${state.experiencia} XP`;
    dom.misionesHud.textContent = `${completadas}/${state.misiones.length} misiones`;
    dom.audio.textContent = state.audioSilenciado ? '🔇' : '🔊';
    dom.audio.setAttribute('aria-pressed', state.audioSilenciado ? 'true' : 'false');
    dom.audio.title = state.audioSilenciado ? 'Activar audio' : 'Silenciar audio';
  }

  function renderSidebar() {
    dom.misiones.textContent = '';
    for (const mision of state.misiones) {
      const item = document.createElement('li');
      const head = document.createElement('div');
      head.className = 'mundo-mision-cabeza';
      const title = document.createElement('strong');
      title.textContent = mision.nombre;
      const badge = document.createElement('span');
      badge.className = 'mundo-mision-estado';
      badge.dataset.estado = mision.estado;
      badge.textContent = Model.questStatusLabel(mision.estado);
      head.append(title, badge);
      item.appendChild(head);

      const desc = document.createElement('p');
      desc.className = 'mundo-mision-desc';
      desc.textContent = mision.descripcion;
      item.appendChild(desc);

      if (mision.recompensa && (mision.recompensa.xp || mision.recompensa.monedas)) {
        const reward = document.createElement('p');
        reward.className = 'mundo-mision-recompensa';
        reward.textContent = `Recompensa: ${mision.recompensa.xp || 0} XP · ${mision.recompensa.monedas || 0} monedas`;
        item.appendChild(reward);
      }

      if (mision.estado === 'lista' && state.puedeGuardar) {
        const action = document.createElement('button');
        action.type = 'button';
        action.className = 'btn cg-btn cg-btn-primary btn-sm';
        action.style.marginTop = '.4rem';
        action.textContent = mision.minijuego ? 'Abrir desafío' : 'Reclamar misión';
        action.addEventListener('click', () => {
          if (mision.minijuego) openMinigame(mision.id);
          else claimQuest(mision.id);
        });
        item.appendChild(action);
      }
      dom.misiones.appendChild(item);
    }

    dom.inventario.textContent = '';
    if (!state.inventario.length) {
      const empty = document.createElement('li');
      empty.className = 'mundo-vacio';
      empty.textContent = 'Aún no has encontrado objetos.';
      dom.inventario.appendChild(empty);
    } else {
      for (const item of state.inventario) {
        const li = document.createElement('li');
        const strong = document.createElement('strong');
        strong.textContent = item.nombre || item.id;
        const small = document.createElement('div');
        small.className = 'mundo-mision-desc';
        small.textContent = item.descripcion || '';
        li.append(strong, small);
        dom.inventario.appendChild(li);
      }
    }

    const academico = config.academico;
    if (academico) {
      dom.academicoTexto.textContent = `Etapa ${academico.etapa_numero}: ${academico.etapa_titulo}. La aldea es una capa motivacional; el progreso académico se consulta en el roadmap.`;
      dom.academicoEnlace.href = academico.url;
      dom.academicoEnlace.textContent = 'Abrir etapa 0 en el roadmap';
    } else {
      dom.academicoTexto.textContent = 'El roadmap no está cargado. Puedes explorar la aldea, pero el vínculo académico aparecerá al cargar ASCENSO.';
    }
  }

  function ensureAudio() {
    if (audioContext) return audioContext;
    const AudioCtor = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtor) return null;
    audioContext = new AudioCtor();
    return audioContext;
  }

  function tone(frequency, duration = 0.06, type = 'square') {
    if (state.audioSilenciado) return;
    const audio = ensureAudio();
    if (!audio) return;
    if (audio.state === 'suspended') audio.resume().catch(() => {});
    const oscillator = audio.createOscillator();
    const gain = audio.createGain();
    oscillator.type = type;
    oscillator.frequency.value = frequency;
    gain.gain.value = 0.035;
    oscillator.connect(gain);
    gain.connect(audio.destination);
    oscillator.start();
    oscillator.stop(audio.currentTime + duration);
  }

  function showDialogue(nombre, texto, action) {
    if (!dom.dialogo) return;
    dom.dialogoNombre.textContent = nombre;
    dom.dialogoTexto.textContent = texto;
    dialogueAction = action || null;
    if (action && dom.dialogoAccion) {
      dom.dialogoAccion.hidden = false;
      dom.dialogoAccion.textContent = action.label;
    } else if (dom.dialogoAccion) {
      dom.dialogoAccion.hidden = true;
    }
    dom.dialogo.hidden = false;
    dom.dialogo.scrollTop = 0;
    const closeButton = document.getElementById('btnMundoDialogoCerrar');
    if (closeButton) closeButton.focus();
  }

  function hideDialogue() {
    if (dom.dialogo) dom.dialogo.hidden = true;
    dialogueAction = null;
  }

  async function interactWith(object) {
    if (!state.puedeGuardar) {
      showDialogue(object.nombre, 'No hay un propietario local configurado. La exploración funciona, pero las misiones y el guardado requieren un perfil local.');
      return;
    }
    try {
      const data = await api(config.endpoints.interactuar, { objeto: object.id });
      applyServerState(data.estado);
      tone(660, 0.05, 'triangle');
      const action = questActionFor(object.id);
      showDialogue(data.interaccion.nombre, data.interaccion.texto, action);
    } catch (error) {
      showDialogue('No se pudo interactuar', error.message);
    }
  }

  function questActionFor(objectId) {
    if (!state.puedeGuardar) return null;
    if (objectId === 'ada') {
      const mision = comandoMision('metodo-principal');
      if (mision && mision.estado === 'lista') {
        return { label: 'Reclamar El método de Ada', run: () => claimQuest('metodo-principal') };
      }
    }
    if (objectId === 'byte') {
      const mision = comandoMision('biblioteca-secundaria');
      if (mision && mision.estado === 'lista') {
        return { label: 'Reclamar Fuentes con criterio', run: () => claimQuest('biblioteca-secundaria') };
      }
    }
    if (objectId === 'guardian') {
      const mision = comandoMision('desafio-depuracion');
      if (mision && mision.estado === 'lista') {
        return { label: 'Abrir desafío de depuración', run: () => openMinigame('desafio-depuracion') };
      }
    }
    return null;
  }

  async function claimQuest(misionId) {
    try {
      const data = await api(config.endpoints.mision, { mision: misionId });
      applyServerState(data.estado);
      tone(880, 0.12, 'triangle');
      hideDialogue();
      showDialogue('Misión completada', `${data.resultado.mensaje} Ganaste ${data.resultado.xp || 0} XP. Las recompensas son motivacionales y no modifican tu progreso académico.`);
    } catch (error) {
      showDialogue('No se pudo completar la misión', error.message);
    }
  }

  function openMinigame(misionId) {
    const mision = comandoMision(misionId);
    if (!mision || !mision.minijuego) return;
    activeQuest = mision;
    hideDialogue();
    dom.formMinijuego.textContent = '';
    for (const pregunta of mision.minijuego.preguntas) {
      const fieldset = document.createElement('fieldset');
      const legend = document.createElement('legend');
      legend.textContent = pregunta.pregunta;
      fieldset.appendChild(legend);
      pregunta.opciones.forEach((opcion, index) => {
        const label = document.createElement('label');
        const input = document.createElement('input');
        input.type = 'radio';
        input.name = pregunta.id;
        input.value = String(index);
        input.required = true;
        label.append(input, document.createTextNode(` ${opcion}`));
        fieldset.appendChild(label);
      });
      dom.formMinijuego.appendChild(fieldset);
    }
    dom.minijuegoError.hidden = true;
    dom.minijuego.hidden = false;
    modalOpen = true;
    const first = dom.formMinijuego.querySelector('input');
    if (first) first.focus();
  }

  function closeMinigame() {
    dom.minijuego.hidden = true;
    dom.minijuegoError.hidden = true;
    modalOpen = false;
    activeQuest = null;
    canvas.focus();
  }

  async function submitMinigame(event) {
    event.preventDefault();
    if (!activeQuest) return;
    const respuestas = {};
    for (const pregunta of activeQuest.minijuego.preguntas) {
      const selected = dom.formMinijuego.querySelector(`input[name="${pregunta.id}"]:checked`);
      if (!selected) {
        dom.minijuegoError.textContent = 'Responde todas las preguntas antes de comprobar.';
        dom.minijuegoError.hidden = false;
        return;
      }
      respuestas[pregunta.id] = Number(selected.value);
    }
    try {
      const data = await api(config.endpoints.mision, {
        mision: activeQuest.id,
        respuestas
      });
      applyServerState(data.estado);
      closeMinigame();
      tone(990, 0.15, 'triangle');
      showDialogue('Desafío superado', `${data.resultado.mensaje} Ganaste ${data.resultado.xp || 0} XP. El servidor validó tus respuestas; no se otorga aprobación académica.`);
    } catch (error) {
      dom.minijuegoError.textContent = error.message;
      dom.minijuegoError.hidden = false;
    }
  }

  function togglePause(force) {
    if (modalOpen) return;
    const next = typeof force === 'boolean' ? force : !paused;
    paused = next;
    dom.pausa.hidden = !paused;
    if (paused) {
      saveNow();
      const button = document.getElementById('btnMundoReanudar');
      if (button) button.focus();
    } else {
      canvas.focus();
    }
  }

  async function saveNow() {
    if (!state.puedeGuardar || saving) return false;
    saving = true;
    try {
      await api(config.endpoints.guardar, {
        region: config.region.id,
        x: Math.round(player.x - 0.5),
        y: Math.round(player.y - 0.5),
        direccion: player.direction,
        tiempo_jugado: Math.floor(state.tiempoJugado),
        audio_silenciado: state.audioSilenciado
      });
      setStatus(`Partida guardada · ${new Date().toLocaleTimeString()}`);
      return true;
    } catch (error) {
      setStatus(`No se pudo guardar: ${error.message}`);
      return false;
    } finally {
      saving = false;
    }
  }

  function scheduleSave() {
    if (!state.puedeGuardar) return;
    if (saveTimer) clearTimeout(saveTimer);
    saveTimer = setTimeout(() => {
      saveTimer = null;
      saveNow();
    }, 700);
  }

  function saveOnExit() {
    if (!state.puedeGuardar) return;
    fetch(config.endpoints.guardar, {
      method: 'POST',
      credentials: 'same-origin',
      keepalive: true,
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken()
      },
      body: JSON.stringify({
        region: config.region.id,
        x: Math.round(player.x - 0.5),
        y: Math.round(player.y - 0.5),
        direccion: player.direction,
        tiempo_jugado: Math.floor(state.tiempoJugado),
        audio_silenciado: state.audioSilenciado
      })
    }).catch(() => {});
  }

  function entityBlocked(x, y) {
    for (const object of map.objects) {
      if (object.tipo !== 'npc') continue;
      if (Model.distance(x, y, object.x + 0.5, object.y + 0.5) < 0.62) return true;
    }
    return false;
  }

  function update(dt) {
    if (paused || modalOpen) return;
    let dx = 0;
    let dy = 0;
    if (keys.has('ArrowLeft') || keys.has('a') || keys.has('A')) dx -= 1;
    if (keys.has('ArrowRight') || keys.has('d') || keys.has('D')) dx += 1;
    if (keys.has('ArrowUp') || keys.has('w') || keys.has('W')) dy -= 1;
    if (keys.has('ArrowDown') || keys.has('s') || keys.has('S')) dy += 1;

    player.moving = dx !== 0 || dy !== 0;
    if (player.moving) {
      state.tiempoJugado += dt;
      const length = Math.hypot(dx, dy) || 1;
      const speed = 3.4;
      const stepX = (dx / length) * speed * dt;
      const stepY = (dy / length) * speed * dt;
      const next = Model.moveWithCollision(map, player.x, player.y, stepX, stepY, 0.3);
      if (!entityBlocked(next.x, player.y)) player.x = next.x;
      if (!entityBlocked(player.x, next.y)) player.y = next.y;
      player.direction = Model.directionFromDelta(dx, dy, player.direction);
      player.frame = Math.floor(elapsed / 160) % 2;
      scheduleSave();
    } else {
      player.frame = 0;
    }
  }

  function drawObject(object, camera) {
    const px = (object.x - camera.x) * Sprites.T;
    const py = (object.y - camera.y) * Sprites.T;
    if (object.tipo === 'npc') {
      Sprites.drawNpc(ctx, px, py, object.color, Math.floor(elapsed / 300) % 2);
    } else {
      Sprites.drawObject(ctx, object.id, px, py, object.color, elapsed);
    }
  }

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const camera = Model.cameraFor(
      { x: player.x, y: player.y },
      VIEW_W, VIEW_H, map.width, map.height
    );
    const startX = Math.max(0, Math.floor(camera.x) - 1);
    const startY = Math.max(0, Math.floor(camera.y) - 1);
    const endX = Math.min(map.width, Math.ceil(camera.x + VIEW_W) + 1);
    const endY = Math.min(map.height, Math.ceil(camera.y + VIEW_H) + 1);

    for (let y = startY; y < endY; y += 1) {
      for (let x = startX; x < endX; x += 1) {
        const px = Math.floor((x - camera.x) * Sprites.T);
        const py = Math.floor((y - camera.y) * Sprites.T);
        Sprites.drawTile(ctx, map.grid[y][x], px, py, elapsed);
      }
    }

    const entities = map.objects.slice().sort((a, b) => a.y - b.y);
    for (const object of entities) {
      if (
        object.x >= startX - 1 && object.x <= endX &&
        object.y >= startY - 1 && object.y <= endY
      ) drawObject(object, camera);
    }

    const playerPx = (player.x - 0.5 - camera.x) * Sprites.T;
    const playerPy = (player.y - 0.5 - camera.y) * Sprites.T;
    Sprites.drawPlayer(ctx, playerPx, playerPy, player.direction, player.frame);

    const nearest = Model.nearestInteractable(player, map.objects, 1.5);
    if (nearest && !paused && !modalOpen) {
      Sprites.drawPrompt(
        ctx,
        (nearest.x - camera.x) * Sprites.T,
        (nearest.y - camera.y) * Sprites.T,
        elapsed
      );
    }

    if (elapsed % 1000 < 80) {
      ctx.fillStyle = 'rgba(15,23,42,.65)';
      ctx.fillRect(8, canvas.height - 22, 128, 14);
      ctx.fillStyle = '#e2e8f0';
      ctx.font = '10px monospace';
      ctx.fillText(Model.formatTime(state.tiempoJugado), 14, canvas.height - 12);
    }
  }

  function loop(timestamp) {
    if (!running) return;
    const dt = lastTime ? Math.min((timestamp - lastTime) / 1000, 0.05) : 0;
    lastTime = timestamp;
    elapsed = timestamp;
    update(dt);
    render();
    requestAnimationFrame(loop);
  }

  function handleKeyDown(event) {
    const tag = (event.target && event.target.tagName || '').toLowerCase();
    if (['input', 'textarea', 'select'].includes(tag)) return;
    if (event.key === 'Escape') {
      if (modalOpen) closeMinigame();
      else togglePause();
      event.preventDefault();
      return;
    }
    if (event.key === 'm' || event.key === 'M') {
      state.audioSilenciado = !state.audioSilenciado;
      renderHud();
      scheduleSave();
      event.preventDefault();
      return;
    }
    if (event.key === 'e' || event.key === 'E' || event.key === 'Enter') {
      if (!dom.dialogo.hidden) {
        if (dialogueAction) dialogueAction.run();
        else hideDialogue();
      } else {
        const nearest = Model.nearestInteractable(player, map.objects, 1.5);
        if (nearest) interactWith(nearest);
      }
      event.preventDefault();
      return;
    }
    if (event.key === ' ') {
      togglePause();
      event.preventDefault();
      return;
    }
    if (['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(event.key)) {
      event.preventDefault();
    }
    keys.add(event.key);
    ensureAudio();
  }

  function handleKeyUp(event) {
    keys.delete(event.key);
  }

  function bindEvents() {
    window.addEventListener('keydown', handleKeyDown);
    window.addEventListener('keyup', handleKeyUp);
    window.addEventListener('blur', () => keys.clear());
    window.addEventListener('pagehide', () => {
      saveOnExit();
      destroy();
    });
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) togglePause(true);
    });
    canvas.addEventListener('click', () => canvas.focus());

    const close = document.getElementById('btnMundoDialogoCerrar');
    const closeX = document.getElementById('btnMundoCerrarDialogo');
    if (close) close.addEventListener('click', hideDialogue);
    if (closeX) closeX.addEventListener('click', hideDialogue);
    if (dom.dialogoAccion) {
      dom.dialogoAccion.addEventListener('click', () => {
        if (dialogueAction) {
          const action = dialogueAction;
          hideDialogue();
          action.run();
        }
      });
    }

    const pause = document.getElementById('btnMundoPausa');
    const resume = document.getElementById('btnMundoReanudar');
    const save = document.getElementById('btnMundoGuardar');
    if (pause) pause.addEventListener('click', () => togglePause());
    if (resume) resume.addEventListener('click', () => togglePause(false));
    if (save) save.addEventListener('click', saveNow);
    if (dom.audio) {
      dom.audio.addEventListener('click', () => {
        state.audioSilenciado = !state.audioSilenciado;
        renderHud();
        scheduleSave();
      });
    }
    if (dom.formMinijuego) dom.formMinijuego.addEventListener('submit', submitMinigame);
    const closeMin = document.getElementById('btnMundoCerrarMinijuego');
    if (closeMin) closeMin.addEventListener('click', closeMinigame);

    document.querySelectorAll('[data-mundo-dir]').forEach((button) => {
      const direction = button.dataset.mundoDir;
      const key = { up: 'ArrowUp', down: 'ArrowDown', left: 'ArrowLeft', right: 'ArrowRight' }[direction];
      const press = (event) => {
        event.preventDefault();
        keys.add(key);
        pointers.add(button);
      };
      const release = () => {
        keys.delete(key);
        pointers.delete(button);
      };
      button.addEventListener('pointerdown', press);
      button.addEventListener('pointerup', release);
      button.addEventListener('pointerleave', release);
      button.addEventListener('pointercancel', release);
    });
    document.querySelectorAll('[data-mundo-action="interact"]').forEach((button) => {
      button.addEventListener('click', () => {
        const nearest = Model.nearestInteractable(player, map.objects, 1.5);
        if (nearest) interactWith(nearest);
      });
    });
  }

  function destroy() {
    if (!running) return;
    running = false;
    keys.clear();
    pointers.clear();
    if (saveTimer) clearTimeout(saveTimer);
    window.removeEventListener('keydown', handleKeyDown);
    window.removeEventListener('keyup', handleKeyUp);
    if (audioContext && audioContext.close) audioContext.close().catch(() => {});
  }

  renderHud();
  renderSidebar();
  bindEvents();
  requestAnimationFrame(loop);
  window.CodeGuardMundoApp = { destroy, saveNow, getState: () => state, player };
})();
