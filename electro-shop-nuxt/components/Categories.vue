<template>
    <b-container>
      <b-row>
        <b-col>
          <h2 class="title">Shop by Categories</h2>
        </b-col>
        <b-col class="text-right">
          <b-button variant="outline-primary">
            <b-icon icon="arrow-left"></b-icon>
          </b-button>
          <b-button variant="outline-primary">
            <b-icon icon="arrow-right"></b-icon>
          </b-button>
        </b-col>
      </b-row>

      <b-row>
        <b-col cols="12" md="4" lg="2" v-for="item in items" :key="item">
          <div class="d-flex flex-column align-items-center justify-content-center">
            <div class="category-image-wrapper">
              <b-img fluid :src="item.image" alt="Product image" />
            </div>
          </div>
          <div class="category-name mt-3 mb-3">{{ item.name }}</div>
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
            name: "Mobile Phones"
          },
          {
            image: "/images/microsoft-surface-go.png",
            name: "Smart TV"
          },
          {
            image: "/images/lg-4k-tv.png",
            name: "Smart Watch"
          },
          {
            image: "/images/samsung-s22-ultra.png",
            name: "Laptops"
          },
          {
            image: "/images/apple-iphone.png",
            name: "Drones"
          },
          {
            image: "/images/bose-headphones.png",
            name: "Headphones"
          }
        ]
      }
    }
  }
</script>

<style scoped>
  .title {
    font: 700 30px/140% Montserrat, sans-serif;
  }

  .category-name {
    color: #101316;
    font: 700 16px/30px Montserrat, sans-serif;
    text-align: center;
  }

  .category-image-wrapper {
    width: 165px;
    height: 165px;
    border-radius: 50%;
    background-color: rgba(165, 169, 172, 0.1);
  }
</style>