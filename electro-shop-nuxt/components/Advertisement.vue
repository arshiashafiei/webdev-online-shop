<template>
  <div class="product-banner">
    <div class="container">
      <img
        src="ad-background.png"
        alt="Apple iPhone 13 Pro Max"
        class="product-image"
      />
      <p class="product-title">Apple iPhone 13 Pro Max</p>
      <p class="product-description">Don't miss the last opportunity</p>
      <b-button class="shop-now-button">
        Shop Now
        <b-icon icon="arrow-right"></b-icon>
      </b-button>
    </div>
  </div>
</template>

<style scoped>
.product-banner {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: start;
  min-height: 500px;
  padding: 80px;
  color: #fff;
  font-weight: 400;
  overflow: hidden;
}

@media (max-width: 991px) {
  .product-banner {
    padding: 0 20px;
  }
}

.product-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.product-title {
  position: relative;
  width: 440px;
  font: 700 40px/56px Montserrat, sans-serif;
}

@media (max-width: 991px) {
  .product-title {
    max-width: 100%;
  }
}

.product-description {
  position: relative;
  font: 18px/167% Montserrat, sans-serif;
}

@media (max-width: 991px) {
  .product-description {
    max-width: 100%;
  }
}

.shop-now-button {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
  border-radius: 10px;
  background-color: #1c4e8e;
  border-color: #1c4e8e;
  font: 16px/30px Montserrat, sans-serif;
  text-decoration: none;
}

@media (max-width: 991px) {
  .shop-now-button {
    margin-left: 10px;
  }
}

.button-icon {
  width: 24px;
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
}
</style>
