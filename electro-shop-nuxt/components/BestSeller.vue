<template>
    <b-container>
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
                  <div>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star" class="star-icon"></b-icon>
                  </div>
                  <div class="product-name">{{ item.name }}</div>
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
</style>