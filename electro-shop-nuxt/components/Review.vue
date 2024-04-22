<template>
    <article class="review">
      <header class="reviewer-info">
        <img src="/review/mark.jpg" alt="Profile picture of Mark Williams" class="profile-picture" />
        <div class="reviewer-details">
          <h3 class="reviewer-name">Mark Williams</h3>
          <div>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
            <b-icon icon="star" class="star-icon"></b-icon>
          </div>
        </div>
      </header>
      <h2 class="review-title">Excellent Product, I Love It 😍</h2>
      <p class="review-content">
        It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.
      </p>
      <footer class="review-meta">
        Review by <span class="reviewer-company">Electro</span>
        Posted on <time class="review-date">Sep 08, 2023</time>
      </footer>
      <hr class="review-separator" />
    </article>
  </template>
  
  <style scoped>
  .review {
    display: flex;
    flex-direction: column;
    font-size: 16px;
    color: var(--Dark-500, #101316);
    font-weight: 400;
    line-height: 30px;
  }
  
  .reviewer-info {
    align-self: start;
    display: flex;
    gap: 10px;
  }
  
  .profile-picture {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    margin: auto 0;
  }
  
  .reviewer-details {
    display: flex;
    flex-direction: column;
    padding: 0 20px;
  }
  
  .reviewer-name {
    font-family: Montserrat, sans-serif;
    margin: 0;
  }
  
  .company-logo {
    width: 100px;
    height: 20px;
    object-fit: contain;
    margin-top: 6px;
  }
  
  .review-title {
    font-family: Montserrat, sans-serif;
    font-weight: 700;
    margin: 10px 0 0;
    width: 100%;
  }
  
  @media (max-width: 991px) {
    .review-title {
      max-width: 100%;
    }
  }
  
  .review-content {
    font-family: Montserrat, sans-serif;
    width: 100%;
    margin: 0;
  }
  
  @media (max-width: 991px) {
    .review-content {
      max-width: 100%;
    }
  }
  
  .review-meta {
    margin: 10px 0 0;
    width: 100%;
    font: 14px/24px Montserrat, sans-serif;
  }
  
  @media (max-width: 991px) {
    .review-meta {
      max-width: 100%;
    }
  }
  
  .reviewer-company {
    color: rgba(16, 19, 22, 1);
  }
  
  .review-date {
    color: rgba(16, 19, 22, 1);
  }
  
  .review-separator {
    background-color: var(--gray-gray-20, rgba(165, 169, 172, 0.2));
    height: 1px;
    border: none;
    margin: 16px 0 0;
    width: 100%;
  }
  
  @media (max-width: 991px) {
    .review-separator {
      max-width: 100%;
    }
  }

  .star-icon {
    color: #FFC11F;
  }
  </style>