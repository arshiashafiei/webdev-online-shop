<template>
    <b-container>
        <ProductMain :product_data="product_data" />
        <ProductDetails :product_data="product_data" />
        <h2 class="mt-3">Related Products</h2>
        <RelatedProducts :product_data="product_data" />
    </b-container>
</template>

<script>
  export default {
    name: 'ProductPage',
    data() {
      return {
        product_id: this.$route.params.id,
        product_data: {}
      }
    },
    methods: {
      async get_product() {
        const res = await this.$axios.$get(`/api/products/${this.product_id}/`)
        this.product_data = res
      }
    },
    mounted() {
      this.get_product()
    }
  }
</script>