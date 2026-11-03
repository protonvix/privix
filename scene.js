// Interactive 3D showcase: a car (paint colours) and a modern house (day / night).
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

const host = document.getElementById("viewer");
const canvas = document.getElementById("viewer-canvas");
const loading = document.getElementById("viewer-loading");
const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 0.9;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const pmrem = new THREE.PMREMGenerator(renderer);
const envMap = pmrem.fromScene(new RoomEnvironment(renderer), 0.04).texture;

const camera = new THREE.PerspectiveCamera(36, 1, 0.1, 100);
const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;
controls.enablePan = false;
controls.minDistance = 4;
controls.maxDistance = 14;
controls.maxPolarAngle = Math.PI * 0.48;
controls.autoRotate = !reduceMotion;
controls.autoRotateSpeed = 1.6;

/* ---------- Car scene ---------- */
const carScene = new THREE.Scene();
carScene.environment = envMap;
const bodyMat = new THREE.MeshPhysicalMaterial({ color: 0xc8102e, metalness: 1, roughness: 0.45, clearcoat: 1, clearcoatRoughness: 0.03 });
const detailsMat = new THREE.MeshStandardMaterial({ color: 0xffffff, metalness: 1, roughness: 0.4 });
const glassMat = new THREE.MeshPhysicalMaterial({ color: 0xffffff, metalness: 0.25, roughness: 0, transmission: 1 });
const wheels = [];
let carReady = false;

function loadCar() {
  const draco = new DRACOLoader();
  draco.setDecoderPath("https://unpkg.com/three@0.160.0/examples/jsm/libs/draco/gltf/");
  const loader = new GLTFLoader();
  loader.setDRACOLoader(draco);
  loader.load("assets/3d/ferrari.glb", (gltf) => {
    const car = gltf.scene.children[0];
    car.getObjectByName("body").material = bodyMat;
    ["rim_fl", "rim_fr", "rim_rr", "rim_rl", "trim"].forEach((n) => (car.getObjectByName(n).material = detailsMat));
    car.getObjectByName("glass").material = glassMat;
    ["wheel_fl", "wheel_fr", "wheel_rl", "wheel_rr"].forEach((n) => wheels.push(car.getObjectByName(n)));
    const shadow = new THREE.TextureLoader().load("assets/3d/ferrari_ao.png");
    const plane = new THREE.Mesh(
      new THREE.PlaneGeometry(0.655 * 4, 1.3 * 4),
      new THREE.MeshBasicMaterial({ map: shadow, blending: THREE.MultiplyBlending, toneMapped: false, transparent: true })
    );
    plane.rotation.x = -Math.PI / 2;
    plane.renderOrder = 2;
    car.add(plane);
    carScene.add(car);
    carReady = true;
    if (mode === "car") loading.hidden = true;
  }, undefined, () => { loading.textContent = "The 3D model could not load. Please refresh the page."; });
}
// Floor glow ring under the car
const ring = new THREE.Mesh(new THREE.RingGeometry(2.6, 2.64, 96), new THREE.MeshBasicMaterial({ color: 0x4f7cff, transparent: true, opacity: 0.6 }));
ring.rotation.x = -Math.PI / 2; ring.position.y = 0.001; carScene.add(ring);
const ring2 = ring.clone(); ring2.scale.setScalar(1.25); ring2.material = ring.material.clone(); ring2.material.opacity = 0.25; carScene.add(ring2);

/* ---------- House scene (built from simple shapes) ---------- */
const houseScene = new THREE.Scene();
houseScene.environment = envMap;
const sun = new THREE.DirectionalLight(0xffffff, 2.2);
sun.position.set(6, 9, 5); sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048);
Object.assign(sun.shadow.camera, { left: -8, right: 8, top: 8, bottom: -8 });
const hemi = new THREE.HemisphereLight(0xdfe8ff, 0x3a3f2a, 0.9);
houseScene.add(sun, hemi);

const M = (o) => new THREE.MeshStandardMaterial(o);
const white = M({ color: 0xf4f4f2, roughness: 0.85 });
const dark = M({ color: 0x2b2f36, roughness: 0.6 });
const wood = M({ color: 0x9a6a3f, roughness: 0.7 });
const windowMat = new THREE.MeshPhysicalMaterial({ color: 0x1b2a3a, metalness: 0.2, roughness: 0.05, emissive: 0xffc977, emissiveIntensity: 0, clearcoat: 1 });
const grass = M({ color: 0x5f8f4e, roughness: 1 });
const stone = M({ color: 0xd9d4ca, roughness: 0.9 });
const water = new THREE.MeshPhysicalMaterial({ color: 0x27a6c9, roughness: 0.05, metalness: 0.1, transmission: 0.2, clearcoat: 1 });
const leaf = M({ color: 0x3f7a3a, roughness: 0.9 });

function box(w, h, d, mat, x, y, z) {
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat);
  m.position.set(x, y, z); m.castShadow = true; m.receiveShadow = true; houseScene.add(m); return m;
}
const ground = new THREE.Mesh(new THREE.CylinderGeometry(6.2, 6.2, 0.2, 72), grass);
ground.position.y = -0.1; ground.receiveShadow = true; houseScene.add(ground);
box(7.4, 0.12, 4.6, stone, 0, 0.06, 0.2);                 // terrace
box(4.6, 1.6, 3.2, white, -0.9, 0.92, -0.2);              // ground floor
box(4.2, 1.4, 3.4, white, 0.7, 2.42, -0.3);               // upper floor (cantilever)
box(4.5, 0.12, 3.7, dark, 0.7, 3.18, -0.3);                // roof slab
box(4.9, 0.1, 3.5, dark, -0.9, 1.77, -0.2);               // first floor slab
box(1.1, 1.6, 3.22, wood, -2.7, 0.92, -0.2);              // wood cladding
box(3.2, 1.1, 0.06, windowMat, -0.6, 0.95, 1.42);         // ground glazing
box(3.6, 0.9, 0.06, windowMat, 0.9, 2.45, 1.42);          // upper glazing
box(0.06, 0.9, 2.2, windowMat, 2.82, 2.45, -0.3);         // side glazing
box(2.8, 0.12, 1.6, stone, 1.9, 0.08, 2.2);               // pool deck
const pool = box(2.4, 0.06, 1.2, water, 1.9, 0.15, 2.2);  // pool
pool.castShadow = false;
for (const [x, z, s] of [[-4.3, 1.9, 1], [-4.6, -1.8, 0.8], [4.4, -1.6, 1.1], [3.6, -3.4, 0.7]]) {
  const trunk = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.09, 0.9 * s, 8), wood);
  trunk.position.set(x, 0.45 * s, z); trunk.castShadow = true; houseScene.add(trunk);
  const crown = new THREE.Mesh(new THREE.IcosahedronGeometry(0.6 * s, 1), leaf);
  crown.position.set(x, 1.15 * s, z); crown.castShadow = true; houseScene.add(crown);
}
const lamp = new THREE.PointLight(0xffc977, 0, 9); lamp.position.set(0, 1.8, 2.2); houseScene.add(lamp);
let night = false;
function setNight(on) {
  night = on;
  houseScene.traverse((o) => { if (o.isMesh && o.material !== windowMat) o.material.envMapIntensity = on ? 0.08 : 1; });
  windowMat.envMapIntensity = on ? 0.3 : 1;
  sun.intensity = on ? 0.15 : 2.2;
  hemi.intensity = on ? 0.18 : 0.9;
  windowMat.emissiveIntensity = on ? 1.6 : 0;
  lamp.intensity = on ? 6 : 0;
  water.emissive = new THREE.Color(on ? 0x0a5a7a : 0x000000);
}

/* ---------- Switching, sizing and rendering ---------- */
let mode = "car";
const views = { car: { pos: [4.6, 1.8, 4.9], target: [0, 0.45, 0] }, house: { pos: [9, 5.2, 9.5], target: [0, 1.3, 0] } };
function setMode(m) {
  mode = m;
  const v = views[m];
  camera.position.set(...v.pos); controls.target.set(...v.target);
  controls.minDistance = m === "car" ? 3.5 : 7; controls.maxDistance = m === "car" ? 12 : 18;
  loading.hidden = m === "house" || carReady;
  host.dataset.mode = m;
}
function resize() {
  const r = canvas.getBoundingClientRect();
  renderer.setSize(r.width, r.height, false);
  camera.aspect = r.width / r.height; camera.updateProjectionMatrix();
}
new ResizeObserver(resize).observe(canvas);

let visible = true;
new IntersectionObserver((e) => (visible = e[0].isIntersecting)).observe(host);
const clock = new THREE.Clock();
renderer.setAnimationLoop(() => {
  if (!visible) return;
  const t = clock.getElapsedTime();
  controls.update();
  if (mode === "car") {
    wheels.forEach((w) => (w.rotation.x = -t * 2 * Math.PI * 0.4 * (reduceMotion ? 0 : 1)));
    ring2.material.opacity = 0.15 + 0.12 * Math.sin(t * 2);
    renderer.render(carScene, camera);
  } else {
    renderer.render(houseScene, camera);
  }
});

/* ---------- Controls in the page ---------- */
document.querySelectorAll("[data-view]").forEach((b) => b.addEventListener("click", () => {
  document.querySelectorAll("[data-view]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
  setMode(b.dataset.view);
}));
document.querySelectorAll("[data-paint]").forEach((b) => b.addEventListener("click", () => {
  document.querySelectorAll("[data-paint]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
  bodyMat.color.set(b.dataset.paint);
}));
document.querySelectorAll("[data-time]").forEach((b) => b.addEventListener("click", () => {
  document.querySelectorAll("[data-time]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
  setNight(b.dataset.time === "night");
}));
const spin = document.getElementById("viewer-spin");
spin.setAttribute("aria-pressed", String(controls.autoRotate));
spin.addEventListener("click", () => { controls.autoRotate = !controls.autoRotate; spin.setAttribute("aria-pressed", String(controls.autoRotate)); });

setMode("car");
resize();
loadCar();
