<template>
  <b-container fluid class="p-0">
    <div class="gray-background">
      <b-container>
        <div class="hero-content">
          <div class="hero-text">
            <div class="hero-heading">
              <h1>
                Great Sound <br />
                With Solo <br />
                Headphone
              </h1>
              <p class="hero-description">
                It is a long established fact that a reader will be distracted
                by the readable content of a page when looking at its layout.
                The point of using Lorem Ipsum.
              </p>
              <button class="shop-now-button">
                <span>Shop Now</span>
                <b-icon icon="arrow-right"></b-icon>
              </button>
            </div>
          </div>
          <div class="hero-image-container">
            <img src="hero.png" alt="Headphone product" class="hero-image" />
          </div>
        </div>
      </b-container>
    </div>
    <Categories />
    <Sales />
    <BestSeller />
    <Advertisement />
    <TopSeller />
    <Shipping />
  </b-container>
</template>

<script>
export default {
  name: "IndexPage",
};
</script>

<style scoped>
.hero-content {
  position: relative;
  margin-top: 10px;
  width: 100%;
  display: flex;
  gap: 20px;
}

@media (max-width: 991px) {
  .hero-content {
    max-width: 100%;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
  }
}

.hero-text {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 44%;
  margin-left: 0;
}

@media (max-width: 991px) {
  .hero-text {
    width: 100%;
  }
}

.hero-heading {
  position: relative;
  display: flex;
  flex-direction: column;
  align-self: stretch;
  color: #101316;
  font-weight: 400;
  line-height: 30px;
  margin: auto 0;
}

@media (max-width: 991px) {
  .hero-heading {
    max-width: 100%;
    margin-top: 40px;
  }
}

.hero-heading h1 {
  font: 700 80px/110px Montserrat, sans-serif;
  margin: 0;
}

@media (max-width: 991px) {
  .hero-heading h1 {
    max-width: 100%;
    font-size: 40px;
    line-height: 61px;
  }
}

.hero-description {
  margin: 10px 0 0;
  font: 18px Montserrat, sans-serif;
}

@media (max-width: 991px) {
  .hero-description {
    max-width: 100%;
  }
}

.shop-now-button {
  display: flex;
  justify-content: center;
  border-radius: 10px;
  background-color: #1c4e8e;
  align-self: start;
  margin-top: 38px;
  gap: 10px;
  font-size: 16px;
  color: #fff;
  padding: 13px 20px;
  border: none;
  cursor: pointer;
}

.arrow-icon {
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
  width: 24px;
  margin: auto 0;
}

.hero-image-container {
  display: flex;
  flex-direction: column;
  line-height: normal;
  width: 56%;
  margin-left: 20px;
}

@media (max-width: 991px) {
  .hero-image-container {
    width: 100%;
  }
}

.hero-image {
  aspect-ratio: 0.81;
  object-fit: contain;
  object-position: center;
  width: 100%;
  flex-grow: 1;
}

@media (max-width: 991px) {
  .hero-image {
    max-width: 100%;
    margin-top: 19px;
  }
}
</style>