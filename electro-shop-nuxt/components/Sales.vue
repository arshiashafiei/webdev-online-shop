<template>
  <b-container>
    <b-row>
      <b-col cols="12" md="12" lg="6">
        <div class="product-card-content">
          <div class="product-card-image-wrapper">
            <b-img fluid src="/sales/laptop.png" alt="MacBook Air M2" class="product-card-image" />
            <div class="product-card-discount">50% OFF</div>
            <div class="product-card-title">MacBook Air M2</div>
            <div class="product-card-description">Don't miss the last opportunity</div>
            <div class="product-card-cta">
              <span class="product-card-cta-text">Shop Now</span>
              <b-icon icon="arrow-right"></b-icon>
            </div>
          </div>
        </div>
      </b-col>

      <b-col cols="12" md="12" lg="6">
        <div class="product-card-content">
          <div class="product-card-image-wrapper">
            <img src="/sales/phone.png" alt="Iphone 14 Pro" class="product-card-image" />
            <div class="product-card-discount">50% OFF</div>
            <div class="product-card-title">Iphone 14 Pro</div>
            <div class="product-card-description">Don't miss the last opportunity</div>
            <div class="product-card-cta">
              <span class="product-card-cta-text">Shop Now</span>
              <b-icon icon="arrow-right"></b-icon>
            </div>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>
  
<style scoped>
  .product-card-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: var(--Dark-500, #101316);
    font-weight: 400;
    line-height: 167%;
  }
  
  @media (max-width: 991px) {
    .product-card-content {
      margin-top: 30px;
    }
  }
  
  .product-card-image-wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: start;
    min-height: 261px;
    padding: 30px 80px 30px 30px;
    background-color: var(--gray-gray-10, rgba(165, 169, 172, 0.1));
    overflow: hidden;
  }
  
  @media (max-width: 991px) {
    .product-card-image-wrapper {
      padding: 0 20px;
    }
  }
  
  .product-card-image {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }
  
  .product-card-discount {
    position: relative;
    padding: 7px 10px;
    border-radius: 5px;
    background-color: var(--primary-primary-10, rgba(28, 78, 142, 0.1));
    color: var(--Primary-500, #1c4e8e);
    font: 12px Montserrat, sans-serif;
  }
  
  .product-card-title {
    position: relative;
    margin-top: 5px;
    font: 700 30px/140% Montserrat, sans-serif;
  }
  
  .product-card-description {
    position: relative;
    margin-top: 10px;
    font: 18px Montserrat, sans-serif;
  }
  
  .product-card-cta {
    position: relative;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 30px;
    padding: 10px 20px;
    border-radius: 10px;
    background-color: var(--Primary-500, #1c4e8e);
    color: var(--White-500, #fff);
    font-size: 16px;
    line-height: 30px;
  }
  
  .product-card-cta-text {
    font-family: Montserrat, sans-serif;
  }
  
  .product-card-cta-icon {
    width: 24px;
    aspect-ratio: 1;
    object-fit: contain;
    object-position: center;
  }
</style>