<template>
  <b-container fluid class="product-image">
    <b-row>
      <b-col>
        <div class="d-flex flex-column align-items-start product-banner">
          <div class="product-title mb-2">Apple iPhone 13 Pro Max</div>
          <div class="product-description mb-3">Don't miss the last opportunity</div>
          <b-button variant="primary" class="d-flex flex-row shop-now-button">
            <div class="button-text mr-3">Shop Now</div>
            <b-icon icon="arrow-right"></b-icon>
          </b-button>
        </div>
      </b-col>
    </b-row>
    <!-- <b-img src="/ad-background.png" alt="Apple iPhone 13 Pro Max" class="" /> -->
  </b-container>
</template>
  
<style scoped>
  .product-banner {
    color: #fff;
    font-weight: 400;
  }
  
  .product-image {
    background-image: url("/ad-background.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
  
  .product-title {
    font: 700 40px/56px Montserrat, sans-serif;
  }
    
  .product-description {
    font: 18px/167% Montserrat, sans-serif;
  }
  
  .button-text {
    font-family: Montserrat, sans-serif;
  }
</style>