async function loadJSON(path) {
  const res = await fetch(path);
  return res.json();
}

function getParam(name) {
  return new URLSearchParams(window.location.search).get(name);
}

async function loadFeatured() {
  const products = await loadJSON("../outputs/data/featured.json");
  renderProducts(products);
}

async function loadCategory() {
  const slug = getParam("c");
  document.getElementById("category-title").innerText = slug;

  const products = await loadJSON(`../outputs/data/categories/${slug}.json`);
  renderProducts(products);
}

async function loadProduct() {
  const slug = getParam("p");
  const products = await loadJSON("../outputs/data/products.json");
  const product = products.find(p => p.slug === slug);

  document.getElementById("product").innerHTML = `
    <h1>${product.title}</h1>
    <img src="${product.image_url}">
    <p>${product.description || ""}</p>
    <a href="${product.affiliate_url}" target="_blank">Buy Now</a>
  `;
}

function renderProducts(products) {
  const container = document.getElementById("products");
  container.innerHTML = "";

  products.forEach(p => {
    container.innerHTML += `
      <div class="card">
        <h3>${p.title}</h3>
        <img src="${p.image_url}">
        <p>$${p.price}</p>
        <a href="product.html?p=${p.slug}">View</a>
      </div>
    `;
  });
}

// Router
if (window.location.pathname.endsWith("index.html")) loadFeatured();
if (window.location.pathname.endsWith("category.html")) loadCategory();
if (window.location.pathname.endsWith("product.html")) loadProduct();
