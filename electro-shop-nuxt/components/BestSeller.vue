<template>
    <b-container class="my-5">
      <b-row class="mb-3">
        <b-col>
          <h2 class="title">Our Bestseller Products</h2>
        </b-col>
        <b-col>
          <b-nav align="right" class="nav">
            <b-nav-item active active-class="active">
              <div class="d-flex flex-column">
                New
                <span class="underline"></span>
              </div>
              
            </b-nav-item>
            <b-nav-item disabled>Featured</b-nav-item>
            <b-nav-item disabled>Top Rated</b-nav-item>
          </b-nav>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="12" lg="4">
<div class="d-flex flex-column">
          <div class="gray-background pl-3 pt-3">
            <h1 class="product-name">Apple iPad Pro Wi-Fi</h1>
            <h2 class="product-price">$1520</h2>
            <div class="d-flex justify-content-end">
              <b-img
                src="/images/apple-ipad-pro.png"
                alt="Apple iPad Pro Wi-Fi"
              />
            </div>
          </div>
        </div>
        </b-col>
        <b-col cols="12" lg="8">
          <b-row>
            <b-col cols="12" md="6" lg="4" v-for="item in items" :key="item">
              <nuxt-link :to="`/product/${item.id}`">
                <div class="d-flex flex-column mb-4">
                  <div class="gray-background d-flex justify-content-center">
                    <b-img fluid :src="item.image_url" alt="Product image" />
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
                <div class="product-price mb-3">${{ item.price }}</div>
              </nuxt-link>
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
          },
          {
            image: "/images/lg-4k-tv.png",
            name: "LG 4K Ultra UHD TV",
            price: "5500.00"
          },
          {
            image: "/images/samsung-s22-ultra.png",
            name: "Samsung Galaxy S22 Ultra",
            price: "1350.00"
          },
          {
            image: "/images/apple-iphone.png",
            name: "Apple iPhone 14 Plus",
            price: "850.00"
          },
          {
            image: "/images/bose-headphones.png",
            name: "Bose QuietComfort 45",
            price: "300.00"
          }
        ]
      }
    },
    methods: {
      async get_products() {
        const res = await this.$axios.$get('/api/products/')
        this.items = res.results
      }
    },
    mounted() {
      this.get_products()
    }
  }
</script>
  
<style scoped>
  .star-icon {
    color: #FFC11F;
  }

  .product-name {
    font-weight: 700;
    line-height: 42px;
    width: 310px;
    margin-top: 12px;
  }

  .product-price {
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