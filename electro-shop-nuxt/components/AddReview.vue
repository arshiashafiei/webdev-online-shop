<template>
  <main class="review-form">
    <h2 class="review-form__title">Add your Review</h2>
    <p class="review-form__rating-label">Your Rating</p>
    <div class="review-form__rating">
      <div
        v-for="rating in [1, 2, 3, 4, 5]"
        :key="rating"
        @click="rate_review(rating)"
        class="star-rating pr-2"
      >
        <b-icon
          v-for="star in Array.from({ length: rating }, (v, k) => k)"
          :key="star"
          :icon="selected_rating === rating ? 'star-fill' : 'star'"
          class="star-icon"
        ></b-icon>
      </div>
    </div>
    <form class="review-form__form">
      <label for="nameInput" class="review-form__label">Name</label>
      <input
        type="text"
        id="nameInput"
        placeholder="Enter Your Name"
        class="review-form__input"
      />

      <label for="emailInput" class="review-form__label">Email Address</label>
      <input
        type="email"
        id="emailInput"
        placeholder="Enter Your Email"
        class="review-form__input"
      />

      <label for="reviewInput" class="review-form__label">Your Review</label>
      <div class="review-form__review-input">
        <b-textarea
          id="reviewInput"
          placeholder="Enter Your Review"
          class="review-form__textarea"
        />
      </div>

      <button type="submit" class="review-form__submit-btn">Submit</button>
    </form>
  </main>
</template>
<script>
export default {
  data() {
    return {
      selected_rating: null,
    };
  },
  methods: {
    rate_review(rating) {
      console.log(`Review Added: ${rating} Star`);
      this.selected_rating = rating;
    },
  },
};
</script>
<style scoped>
.review-form {
  display: flex;
  flex-direction: column;
}

.review-form__title {
  color: var(--Dark-500, #101316);
  font: 700 20px/150% Montserrat, sans-serif;
}

.review-form__rating-label {
  color: var(--Dark-500, #101316);
  margin-top: 20px;
  font: 400 16px/30px Montserrat, sans-serif;
}

.review-form__rating {
  align-self: start;
  display: flex;
  margin-top: 10px;
  gap: 10px;
  padding: 0 20px;
}

.review-form__star {
  width: 20px;
  aspect-ratio: 1;
  object-fit: auto;
  object-position: center;
}

.review-form__rating-separator {
  width: 1px;
  height: 20px;
  background-color: var(--gray-gray-20, rgba(165, 169, 172, 0.2));
}

.review-form__stars {
  width: 40px;
  aspect-ratio: 2;
  object-fit: auto;
  object-position: center;
}

.review-form__label {
  color: var(--Dark-500, #101316);
  margin-top: 27px;
  font: 400 12px/167% Montserrat, sans-serif;
}

.review-form__input {
  width: 100%;
  border: 1px solid rgba(165, 169, 172, 0.2);
  border-radius: 10px;
  padding: 23px 16px;
  margin-top: 8px;
  color: var(--gray-gray-80, rgba(165, 169, 172, 0.8));
  font: 400 16px/187.5% Montserrat, sans-serif;
}

.review-form__review-input {
  position: relative;
  margin-top: 5px;
}

.review-form__textarea {
  width: 100%;
  min-height: 150px;
  border: 1px solid rgba(165, 169, 172, 0.2);
  border-radius: 10px;
  padding: 25px 16px;
  color: var(--gray-gray-80, rgba(165, 169, 172, 0.8));
  font: 400 16px/187.5% Montserrat, sans-serif;
  resize: vertical;
}

.review-form__textarea-icon {
  position: absolute;
  right: 16px;
  bottom: 16px;
  width: 13px;
  aspect-ratio: 0.93;
  object-fit: auto;
  object-position: center;
}

.review-form__submit-btn {
  align-self: start;
  margin-top: 30px;
  padding: 13px 20px;
  border: none;
  border-radius: 10px;
  background-color: var(--Primary-500, #1c4e8e);
  color: var(--White-500, #fff);
  font: 400 16px/30px Montserrat, sans-serif;
  cursor: pointer;
}

@media (max-width: 991px) {
  .review-form__title,
  .review-form__rating-label {
    max-width: 100%;
  }

  .review-form__input {
    max-width: 100%;
    padding-right: 20px;
  }

  .review-form__textarea {
    max-width: 100%;
  }

  .review-form__textarea-icon {
    margin-top: 40px;
  }

  .review-form__submit-btn {
    white-space: initial;
  }
}

.star-rating {
  border-right: 1px solid var(--gray-gray-20, rgba(165, 169, 172));
}

.star-rating:last-child {
  border: none !important;
}
</style>
