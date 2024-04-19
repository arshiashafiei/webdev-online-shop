<template>
    <b-container>
      <b-row>
        <b-col>
          <h2 class="title">Our Bestseller Products</h2>
        </b-col>
        <b-col>
          <b-nav align="right" class="nav">
            <b-nav-item class="active">
              <div class="d-flex flex-column">
                New
                <span class="underline"></span>
              </div>
              
            </b-nav-item>
            <b-nav-item>Featured</b-nav-item>
            <b-nav-item>Top Rated</b-nav-item>
          </b-nav>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="12" lg="4">
          <div class="d-flex flex-column">
            <div class="product-name">Apple iPad Pro <br />Wi-Fi</div>
            <div class="product-price">$1520</div>
            <div>
              <b-img fluid src="/images/apple-ipad-pro.png" alt="Apple iPad Pro Wi-Fi" />
            </div>
          </div>
        </b-col>
        <b-col cols="12" lg="8">
          <b-row>
            <b-col cols="12" md="6" lg="4" v-for="item in items" :key="item">
              <div class="d-flex flex-column mb-4">
                    <div class="">
                      <b-img fluid :src="item.image" alt="Product image" />
                    </div>
                  </div>
                  <div class="product-name">{{ item.name }}</div>
                  <div>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star" class="star-icon"></b-icon>
                  </div>
                  <div class="product-price">${{ item.price }}</div>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
</template>
  
  <script>
  export default {
    data() {
      return {
        items: [
          {
            image: "/images/apple-ipad-mini.png",
            name: "Apple iPad Mini 6 Wi-Fi",
            price: "500.00"
          },
          {
            image: "/images/microsoft-surface-go.png",
            name: "Microsoft Surface Go",
            price: "399.00"
          }
        ]
      }
    }
  }
  </script>
  
<style scoped>
  .star-icon {
    color: #FFC11F;
  }

  .product-name {
    font-family: Montserrat, sans-serif;
    font-weight: 700;
    line-height: 42px;
    width: 310px;
    margin-top: 12px;
  }

  .product-price {
    font-family: Montserrat, sans-serif;
    font-weight: 400;
    line-height: 140%;
  }
  
  @media (max-width: 991px) {
    .product-price {
      margin-bottom: 40px;
    }
  }

  .active {
    color: #1c4e8e;
  }

  .underline {
    height: 1px;
    background-color: #1c4e8e;
  }

  .nav {
    font-size: 20px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .title {
    font: 700 30px/140% Montserrat, sans-serif;
  }
</style>