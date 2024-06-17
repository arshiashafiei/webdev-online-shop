<template>
    <main class="product-description">
      <b-tabs content-class="mt-3">
        <b-tab title="Descriptions" active>
          <p class="product-description__text">
            {{ product_data.description }}
          </p>
        </b-tab>
        <b-tab title="Additional Information">
          <ProductInfo />
        </b-tab>
        <b-tab title="Reviews">
          <h3 class="mb-4">Customer Reviews</h3>
          <Review />
          <AddReview />
        </b-tab>
      </b-tabs>
    </main>
</template>

<script>
export default {
  props: {
    product_data: Object
  },
}
</script>
  
<style scoped>
  .product-description {
    display: flex;
    flex-direction: column;
  }
  
  .product-description__nav {
    align-self: start;
    display: flex;
    padding-right: 20px;
    gap: 20px;
    font-size: 20px;
    color: var(--Dark-500, #101316);
    font-weight: 400;
    line-height: 150%;
    justify-content: space-between;
  }
  
  @media (max-width: 991px) {
    .product-description__nav {
      flex-wrap: wrap;
    }
  }
  
  .product-description__nav-link--active {
    color: var(--Primary-500, #1c4e8e);
    font-weight: 700;
  }
  
  .product-description__underline {
    display: flex;
    margin-top: 11px;
    gap: 0px;
  }
  
  @media (max-width: 991px) {
    .product-description__underline {
      flex-wrap: wrap;
    }
  }
  
  .product-description__underline-active {
    background-color: var(--Primary-500, #1c4e8e);
    width: 131px;
    height: 3px;
  }
  
  .product-description__underline-inactive {
    background-color: var(--gray-gray-20, rgba(165, 169, 172, 0.2));
    align-self: start;
    min-height: 1px;
    width: 100%;
    flex-grow: 1;
    flex-basis: 0;
  }
  
  @media (max-width: 991px) {
    .product-description__underline-inactive {
      max-width: 100%;
    }
  }
  
  .product-description__text {
    color: var(--Dark-500, #101316);
    margin-top: 20px;
    width: 100%;
    font: 400 16px/30px Montserrat, sans-serif;
  }
  
  @media (max-width: 991px) {
    .product-description__text {
      max-width: 100%;
    }
  }
</style>