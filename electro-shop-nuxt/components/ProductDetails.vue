<template>
    <main class="product-description">
      <b-tabs content-class="mt-3">
        <b-tab title="Descriptions" active>
          <p class="product-description__text">
            It is a long established fact that a reader will be distracted by the
            readable content of a page when looking at its layout. The point of
            using Lorem Ipsum is that it has a more-or-less normal distribution of
            letters, as opposed to using 'Content here, content here', making it
            look like readable English. Many desktop publishing packages and web
            page editors now use Lorem Ipsum as their default model text, and a
            search for 'lorem ipsum' will uncover many web sites still in their
            infancy.
            <br /><br />
            Various versions have evolved over the years, sometimes by accident,
            sometimes on purpose (injected humour and the like).
          </p>
        </b-tab>
        <b-tab title="Additional Information">
          <p>Additional Information</p>
        </b-tab>
        <b-tab title="Reviews">
          <h3>Customer Reviews</h3>
          <Review />
          <AddReview />
        </b-tab>
      </b-tabs>
      <div class="product-description__underline">
        <div class="product-description__underline-active"></div>
        <div class="product-description__underline-inactive"></div>
      </div>
    </main>
</template>
  
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
  
  .product-description__nav-link {
    font-family: Montserrat, sans-serif;
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