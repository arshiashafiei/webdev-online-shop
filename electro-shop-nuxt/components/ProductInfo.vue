<template>
    <main class="product-details">
      <section class="product-info">
        <div class="info-labels">
          <p class="label">Brand</p>
          <p class="label">Item Height</p>
          <p class="label">Item Width</p>
          <p class="label">Screen Size</p>
          <p class="label">Model Number</p>
          <p class="label">RAM Size</p>
          <p class="label">Operating System</p>
        </div>
        <div class="info-values ml-3">
          <p class="value">Apple</p>
          <p class="value">65 CM</p>
          <p class="value">31.4 CM</p>
          <p class="value">6.5 Inch</p>
          <p class="value">MF841HN/A</p>
          <p class="value">6 GB</p>
          <p class="value">ios 17</p>
        </div>
      </section>
    </main>
  </template>
  
  <style scoped>
  .product-details {
    display: flex;
    flex-direction: column;
    align-items: start;
    color: var(--Dark-500, #101316);
  }
  
  .product-nav {
    display: flex;
    gap: 20px;
    font-size: 20px;
    font-weight: 400;
    justify-content: space-between;
    padding: 0 20px;
  }
  
  @media (max-width: 991px) {
    .product-nav {
      flex-wrap: wrap;
    }
  }
  
  .nav-link {
    font-family: Montserrat, sans-serif;
    text-decoration: none;
    color: inherit;
  }
  
  .nav-link.active {
    color: var(--Primary-500, #1c4e8e);
    font-weight: 700;
  }
  
  .nav-underline {
    background-color: var(--Primary-500, #1c4e8e);
    width: 240px;
    height: 3px;
    margin: 11px 0 0 155px;
  }
  
  @media (max-width: 991px) {
    .nav-underline {
      margin-left: 10px;
    }
  }
  
  .separator {
    background-color: var(--gray-gray-20, rgba(165, 169, 172, 0.2));
    border: none;
    height: 1px;
    width: 100%;
    margin: 0;
  }
  
  .product-info {
    display: flex;
    margin-top: 6px;
    justify-content: space-between;
  }
  
  .info-labels {
    display: flex;
    flex-direction: column;
    font-size: 18px;
    font-weight: 700;
  }
  
  .info-values {
    display: flex;
    flex-direction: column;
    font-size: 16px;
    font-weight: 400;
  }
  
  .label,
  .value {
    font-family: Montserrat, sans-serif;
    margin-top: 6px;
  }
  
  .label:first-child,
  .value:first-child {
    margin-top: 0;
  }
  </style>