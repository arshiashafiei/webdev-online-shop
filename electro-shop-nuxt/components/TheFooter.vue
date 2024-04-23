<template>
  <div class="footer-top">
    <div class="footer-content">
      <div class="footer-info px-2">
        <div class="contact-info">
          <img src="/logo-white.svg" alt="Electro logo" class="logo" />
          <div class="phone-number">
            <img src="/icons/calling-icon.svg" alt="Phone icon" class="icon" />
            <div class="number">(316) 555-0116</div>
          </div>
          <div class="email">
            <img src="/icons/mail-icon.svg" alt="Email icon" class="icon" />
            <div class="email-address">electro@example.com</div>
          </div>
          <div class="address">
            <img
              src="/icons/location-icon.svg"
              alt="Location icon"
              class="icon"
            />
            <div class="address-text">
              4140 Parker Rd. Allentown, <br />New Mexico 31134
            </div>
          </div>
        </div>

        <div class="account-links">
          <h3 class="title">Information</h3>
          <a href="#" class="link">My Account</a>
          <a href="#" class="link">Login</a>
          <a href="#" class="link">My Cart</a>
          <a href="#" class="link">My Wishlist</a>
          <a href="#" class="link">Checkout</a>
        </div>

        <div class="service-links">
          <h3 class="title">Service</h3>
          <a href="#" class="link">About Us</a>
          <a href="#" class="link">Careers</a>
          <a href="#" class="link">Delivery Information</a>
          <a href="#" class="link">Privacy Policy</a>
          <a href="#" class="link">Terms &amp; Conditions</a>
        </div>

        <div class="subscribe-section">
          <h3 class="title">Subscribe</h3>
          <p class="description">
            Enter your email below to be the first to know about new
            collections.
          </p>
          <form class="subscribe-form">
            <div class="input-wrapper">
              <img src="/icons/mail-icon.svg" alt="Email icon" class="icon" />
              <label for="email" class="visually-hidden">Your Email</label>
              <input
                type="email"
                id="email"
                placeholder="Your Email"
                class="email-input"
              />
            </div>
            <button type="submit" class="submit-btn">
              <img
                src="/icons/arrow-right-icon.svg"
                alt="Send icon"
                class="icon"
              />
            </button>
          </form>
        </div>
      </div>

      <div class="footer-divider"></div>

      <div class="footer-bottom">
        <div class="pay-icons">
          <img src="/icons/visa-icon.svg" alt="Visa" class="pay-icon" />
          <img
            src="/icons/mastercard-icon.svg"
            alt="MasterCard"
            class="pay-icon"
          />
          <img
            src="/icons/googlepay-icon.svg"
            alt="GooglePay"
            class="pay-icon"
          />
          <img src="/icons/amex-icon.svg" alt="Amex" class="pay-icon" />
          <img src="/icons/paypal-icon.svg" alt="Paypal" class="pay-icon" />
        </div>

        <div class="copyright">&copy;2023 Electro All Rights are reserved️</div>

        <div class="social-icons">
          <a href="#"
            ><img
              src="/icons/facebook-icon.svg"
              alt="Facebook icon"
              class="icon"
          /></a>
          <a href="#"
            ><img
              src="/icons/instagram-icon.svg"
              alt="Instagram icon"
              class="icon"
          /></a>
          <a href="#"
            ><img src="/icons/twitter-icon.svg" alt="Twitter icon" class="icon"
          /></a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.footer {
  display: flex;
  justify-content: center;
}

.footer-top {
  background-color: #1c4e8e;
  width: 100%;
  padding: 2rem 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.footer-content {
  max-width: 1140px;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.footer-info {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  font-size: 16px;
  color: #fff;
  font-weight: 400;
  line-height: 30px;
}

.contact-info {
  display: flex;
  flex-direction: column;
}

.logo {
  width: 203px;
  max-width: 100%;
  aspect-ratio: 5;
  object-fit: auto;
  object-position: center;
}

.phone-number,
.email,
.address {
  display: flex;
  gap: 10px;
  margin-top: 16px;
}

.icon {
  width: 24px;
  aspect-ratio: 1;
  object-fit: auto;
  object-position: center;
  margin: auto 0;
}

.pay-icon {
  width: 36px;
  aspect-ratio: 1;
  object-fit: auto;
  object-position: center;
  margin: auto 0;
}

.account-links,
.service-links {
  display: flex;
  flex-direction: column;
}

.title {
  font-family: Montserrat, sans-serif;
  font-weight: 700;
  margin-bottom: 10px;
}

.link {
  font-family: Montserrat, sans-serif;
  margin-top: 10px;
  color: #fff;
  text-decoration: none;
}

.subscribe-section {
  display: flex;
  flex-direction: column;
}

.description {
  font-family: Montserrat, sans-serif;
  margin-top: 10px;
}

.subscribe-form {
  background-color: var(--gray-gray-10, rgba(165, 169, 172, 0.1));
  border-radius: 10px;
  padding: 13px 16px;
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.input-wrapper {
  display: flex;
  gap: 10px;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.email-input {
  font-family: Montserrat, sans-serif;
  border: none;
  background: transparent;
  color: var(--White-500, #fff);
}

.email-input::placeholder {
  color: var(--White-500, #fff);
  opacity: 1;
}

.submit-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.footer-divider {
  height: 1px;
  background-color: rgba(165, 169, 172, 0.2);
  margin-top: 64px;
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  margin-top: 16px;
  width: 100%;
}

.copyright {
  color: #fff;
  text-align: center;
  flex-grow: 1;
  font: 400 16px/187.5% Montserrat, sans-serif;
}

.social-icons {
  display: flex;
  gap: 20px;
}

.pay-icons {
  display: flex;
  gap: 10px;
}

@media (max-width: 991px) {
    .footer-info {
        flex-direction: column;
    }
    
    .footer-bottom {
        flex-direction: column;
    }

    .footer-top {
        padding: 1rem;
    }
}
</style>
