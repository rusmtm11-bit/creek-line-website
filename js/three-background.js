// Инициализация сцены, камеры и рендерера
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
document.getElementById('bg-canvas').appendChild(renderer.domElement);

// Настройка камеры
camera.position.set(0, 2, 8);
camera.lookAt(0, 0, 0);

// --- Создание центральной энергетической сферы ---
const coreGeometry = new THREE.IcosahedronGeometry(1.2, 0);
const coreMaterial = new THREE.MeshStandardMaterial({
    color: 0x3b82f6,
    emissive: 0x1e3a8a,
    emissiveIntensity: 0.8,
    roughness: 0.3,
    metalness: 0.7,
    flatShading: false
});
const coreSphere = new THREE.Mesh(coreGeometry, coreMaterial);
scene.add(coreSphere);

// --- Внешняя вращающаяся решетка (Wireframe) ---
const wireframeGeometry = new THREE.IcosahedronGeometry(1.5, 0);
const wireframeMaterial = new THREE.MeshBasicMaterial({
    color: 0x06b6d4,
    wireframe: true,
    transparent: true,
    opacity: 0.3
});
const wireframeSphere = new THREE.Mesh(wireframeGeometry, wireframeMaterial);
scene.add(wireframeSphere);

// --- Парящие энергетические частицы (Particle System) ---
const particlesGeometry = new THREE.BufferGeometry();
const particlesCount = 1500;
const posArray = new Float32Array(particlesCount * 3);

for(let i = 0; i < particlesCount; i++) {
    // Распределяем частицы по сфере радиусом от 3 до 6
    const radius = 3 + Math.random() * 3;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(2 * Math.random() - 1);
    
    posArray[i*3] = radius * Math.sin(phi) * Math.cos(theta);
    posArray[i*3+1] = radius * Math.sin(phi) * Math.sin(theta);
    posArray[i*3+2] = radius * Math.cos(phi);
}
particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

const particlesMaterial = new THREE.PointsMaterial({
    size: 0.05,
    color: 0x3b82f6,
    transparent: true,
    opacity: 0.6,
    blending: THREE.AdditiveBlending
});
const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particlesMesh);

// --- Вращающиеся энергетические кольца (Torus) ---
const ringMaterial = new THREE.MeshStandardMaterial({
    color: 0x06b6d4,
    emissive: 0x0f2b5e,
    emissiveIntensity: 0.5,
    metalness: 0.8,
    roughness: 0.2,
    transparent: true,
    opacity: 0.7
});

const ring1 = new THREE.Mesh(new THREE.TorusGeometry(2.2, 0.05, 64, 200), ringMaterial);
const ring2 = new THREE.Mesh(new THREE.TorusGeometry(2.6, 0.05, 64, 200), ringMaterial);
const ring3 = new THREE.Mesh(new THREE.TorusGeometry(3.0, 0.05, 64, 200), ringMaterial);

ring1.rotation.x = Math.PI / 2;
ring2.rotation.z = Math.PI / 3;
ring3.rotation.x = Math.PI / 4;
ring3.rotation.z = Math.PI / 4;

scene.add(ring1);
scene.add(ring2);
scene.add(ring3);

// --- Освещение для создания объема и драматизма ---
// Ambient light
const ambientLight = new THREE.AmbientLight(0x404060);
scene.add(ambientLight);
// Основной направленный свет
const dirLight = new THREE.DirectionalLight(0xffffff, 1);
dirLight.position.set(1, 2, 1);
scene.add(dirLight);
// Задняя подсветка для контраста
const backLight = new THREE.PointLight(0x3b82f6, 0.5);
backLight.position.set(0, 0, -3);
scene.add(backLight);
// Динамический центральный свет
const coreLight = new THREE.PointLight(0x06b6d4, 1, 10);
coreLight.position.set(0, 0, 0);
scene.add(coreLight);

// Дополнительные звезды на заднем плане
const starGeometry = new THREE.BufferGeometry();
const starCount = 800;
const starPositions = new Float32Array(starCount * 3);
for (let i = 0; i < starCount; i++) {
    starPositions[i*3] = (Math.random() - 0.5) * 200;
    starPositions[i*3+1] = (Math.random() - 0.5) * 100;
    starPositions[i*3+2] = (Math.random() - 0.5) * 80 - 40;
}
starGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
const starMaterial = new THREE.PointsMaterial({ color: 0xffffff, size: 0.1, transparent: true, opacity: 0.5 });
const stars = new THREE.Points(starGeometry, starMaterial);
scene.add(stars);

// --- Анимация ---
let time = 0;

function animate() {
    requestAnimationFrame(animate);
    time += 0.005;

    // Вращение основных элементов
    coreSphere.rotation.y = time * 0.5;
    coreSphere.rotation.x = Math.sin(time * 0.3) * 0.2;
    wireframeSphere.rotation.y = time * 0.3;
    wireframeSphere.rotation.x = time * 0.2;
    particlesMesh.rotation.y = time * 0.05;
    particlesMesh.rotation.x = time * 0.03;
    
    // Вращение колец
    ring1.rotation.z += 0.005;
    ring2.rotation.x += 0.003;
    ring2.rotation.y += 0.004;
    ring3.rotation.y += 0.002;
    ring3.rotation.x += 0.003;

    // Пульсация центрального света
    const intensity = 0.8 + Math.sin(time * 5) * 0.3;
    coreLight.intensity = intensity;
    
    // Едва заметное движение камеры
    camera.position.x += (0 - camera.position.x) * 0.05;
    camera.position.y += (Math.sin(time * 0.2) * 0.1 - camera.position.y) * 0.05;
    camera.lookAt(0, 0, 0);

    renderer.render(scene, camera);
}

animate();

// --- Адаптация под размер окна ---
window.addEventListener('resize', onWindowResize, false);
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}
