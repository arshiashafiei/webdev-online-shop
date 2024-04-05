<template>
    <div class="footer">
      <section class="footer-child" />
      <section class="frame-group">
        <div class="logo-text-parent">
          <img class="logo-text1" loading="lazy" alt="" src="/logo--text1.svg" />
          <div class="call-parent">
            <div class="call">
              <div class="visa-icon">
                <img
                  class="huge-iconcommunicationoutlin"
                  loading="lazy"
                  alt=""
                  src="/hugeiconcommunicationoutlinecalling.svg"
                />
              </div>
              <div class="google-pay-icon">(316) 555-0116</div>
            </div>
            <div class="mail">
              <div class="call-button">
                <div class="huge-iconsocialoutlinegmail">
                  <div class="gmail-icon" />
                  <img
                    class="your-email-label"
                    loading="lazy"
                    alt=""
                    src="/vector-3014.svg"
                  />
                </div>
              </div>
              <div class="electroexamplecom">electro@example.com</div>
            </div>
            <div class="address">
              <img
                class="huge-icondeviceoutlinelocat"
                loading="lazy"
                alt=""
                src="/hugeicondeviceoutlinelocation.svg"
              />
              <div class="parker-rd-allentown-container">
                <p class="parker-rd-allentown">4140 Parker Rd. Allentown,</p>
                <p class="new-mexico-31134">New Mexico 31134</p>
              </div>
            </div>
          </div>
        </div>
        <div class="information">
          <b class="information1">Information</b>
          <div class="my-account-parent">
            <div class="my-account">My Account</div>
            <div class="login">Login</div>
            <div class="my-cart">My Cart</div>
            <div class="my-wishlist">My Wishlist</div>
            <div class="checkout">Checkout</div>
          </div>
        </div>
        <div class="service">
          <b class="service1">Service</b>
          <div class="about-us-parent">
            <div class="about-us1">About Us</div>
            <div class="careers">Careers</div>
            <div class="delivery-information">Delivery Information</div>
            <div class="privacy-policy">Privacy Policy</div>
            <div class="terms-conditions">Terms & Conditions</div>
          </div>
        </div>
        <div class="subscribe">
          <div class="facebook-icon">
            <b class="subscribe1">Subscribe</b>
            <div class="enter-your-email">
              Enter your email below to be the first to know about new
              collections.
            </div>
          </div>
          <div class="mail1">
            <div class="frame-container">
              <div class="huge-iconsocialoutlinegmail-parent">
                <div class="huge-iconsocialoutlinegmail1">
                  <div class="mastercard-payment-method" />
                  <img
                    class="google-pay-payment-method"
                    alt=""
                    src="/vector-3014.svg"
                  />
                </div>
                <div class="your-email">Your Email</div>
              </div>
              <img
                class="huge-iconarrowsoutlinearrow"
                alt=""
                src="/hugeiconarrowsoutlinearrowright@2x.png"
              />
            </div>
          </div>
        </div>
      </section>
      <div class="rectangle-parent">
        <div class="frame-child" />
        <div class="footer-container-parent">
          <div class="footer-container">
            <div class="payment-methodvisa-parent">
              <img
                class="payment-methodvisa-icon"
                loading="lazy"
                alt=""
                src="/payment-methodvisa.svg"
              />
              <img
                class="payment-methodmastercard-icon"
                loading="lazy"
                alt=""
                src="/payment-methodmastercard.svg"
              />
              <img
                class="payment-methodgooglepay-icon"
                loading="lazy"
                alt=""
                src="/payment-methodgooglepay.svg"
              />
              <img
                class="payment-methodamex-icon"
                loading="lazy"
                alt=""
                src="/payment-methodamex.svg"
              />
              <img
                class="payment-methodpaypal-icon"
                loading="lazy"
                alt=""
                src="/payment-methodpaypal.svg"
              />
            </div>
            <div class="electro-all-rights">
              ©2023 Electro All Rights are reserved️
            </div>
          </div>
          <div class="instagram-instances">
            <img
              class="huge-iconsocialsolidfaceboo"
              loading="lazy"
              alt=""
              src="/hugeiconsocialsolidfacebook.svg"
            />
            <img
              class="huge-iconsocialsolidinstagr"
              loading="lazy"
              alt=""
              src="/hugeiconsocialsolidinstagram@2x.png"
            />
            <img
              class="huge-iconsocialsolidtwitter"
              loading="lazy"
              alt=""
              src="/hugeiconsocialsolidtwitter.svg"
            />
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    import { defineComponent } from "vue";
  
    export default defineComponent({
      name: "Footer",
    });
</script>

<style scoped>
    .footer-child {
      width: 100%;
      height: 100%;
      position: absolute;
      margin: 0 !important;
      top: 0px;
      right: 0px;
      bottom: 0px;
      left: 0px;
      background-color: var(--primary-500);
    }
    .logo-text1 {
      width: 202.8px;
      height: 40px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      z-index: 1;
    }
    .huge-iconcommunicationoutlin {
      width: 24px;
      height: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .visa-icon {
      height: 27px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-10xs) 0px 0px;
      box-sizing: border-box;
    }
    .google-pay-icon {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 105px;
    }
    .call {
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      z-index: 1;
    }
    .gmail-icon {
      position: absolute;
      height: 81.25%;
      width: 89.58%;
      top: 9.58%;
      right: 5%;
      bottom: 9.17%;
      left: 5.42%;
      border-radius: var(--br-9xs);
      border: 1.5px solid var(--white-500);
      box-sizing: border-box;
    }
    .your-email-label {
      position: absolute;
      height: 33.33%;
      width: 83.33%;
      top: 29.17%;
      right: 8.33%;
      bottom: 37.5%;
      left: 8.33%;
      max-width: 100%;
      overflow: hidden;
      max-height: 100%;
      z-index: 1;
    }
    .huge-iconsocialoutlinegmail {
      width: 24px;
      height: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .call-button {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-10xs) 0px 0px;
    }
    .electroexamplecom {
      position: relative;
      line-height: 30px;
      white-space: nowrap;
    }
    .mail {
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      z-index: 1;
    }
    .huge-icondeviceoutlinelocat {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .parker-rd-allentown {
      margin: 0;
    }
    .new-mexico-31134 {
      margin: 0;
    }
    .parker-rd-allentown-container {
      position: relative;
      line-height: 30px;
    }
    .address {
      flex: 1;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      z-index: 1;
    }
    .call-parent {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-base);
    }
    .logo-text-parent {
      height: 222px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-11xl);
    }
    .information1 {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 100px;
    }
    .my-account {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 96px;
    }
    .login {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 46px;
    }
    .my-cart {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 63px;
    }
    .my-wishlist {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 92px;
    }
    .checkout {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 78px;
    }
    .my-account-parent {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
    }
    .information {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      z-index: 1;
    }
    .service1 {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 62px;
    }
    .about-us1 {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 75px;
    }
    .careers {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 61px;
    }
    .delivery-information {
      position: relative;
      line-height: 30px;
    }
    .privacy-policy {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 109px;
    }
    .terms-conditions {
      position: relative;
      line-height: 30px;
    }
    .about-us-parent {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
    }
    .service {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      z-index: 1;
    }
    .subscribe1 {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 83px;
    }
    .enter-your-email {
      align-self: stretch;
      position: relative;
      line-height: 30px;
    }
    .facebook-icon {
      align-self: stretch;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
    }
    .mastercard-payment-method {
      position: absolute;
      height: 81.25%;
      width: 89.58%;
      top: 9.58%;
      right: 5%;
      bottom: 9.17%;
      left: 5.42%;
      border-radius: var(--br-9xs);
      border: 1.5px solid var(--white-500);
      box-sizing: border-box;
    }
    .google-pay-payment-method {
      position: absolute;
      height: 33.33%;
      width: 83.33%;
      top: 29.17%;
      right: 8.33%;
      bottom: 37.5%;
      left: 8.33%;
      max-width: 100%;
      overflow: hidden;
      max-height: 100%;
      z-index: 1;
    }
    .huge-iconsocialoutlinegmail1 {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .your-email {
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 87px;
    }
    .huge-iconsocialoutlinegmail-parent {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-start;
      gap: var(--gap-3xs);
    }
    .huge-iconarrowsoutlinearrow {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      object-fit: contain;
    }
    .frame-container {
      align-self: stretch;
      flex: 1;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      gap: var(--gap-xl);
    }
    .mail1 {
      align-self: stretch;
      height: 56px;
      border-radius: var(--br-3xs);
      background-color: var(--gray-gray-10);
      overflow: hidden;
      flex-shrink: 0;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-smi) var(--padding-base);
      box-sizing: border-box;
    }
    .subscribe {
      width: 322px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      max-width: 100%;
      z-index: 1;
    }
    .frame-group {
      width: 1140px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: space-between;
      max-width: 100%;
      gap: var(--gap-xl);
      text-align: left;
      font-size: var(--body-1-regular-size);
      color: var(--white-500);
      font-family: var(--body-1-regular);
    }
    .frame-child {
      align-self: stretch;
      height: 1px;
      position: relative;
      background-color: var(--gray-gray-20);
      z-index: 1;
    }
    .payment-methodvisa-icon {
      height: 24px;
      width: 36px;
      position: relative;
      border-radius: var(--br-10xs-4);
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .payment-methodmastercard-icon {
      height: 24px;
      width: 36px;
      position: relative;
      border-radius: var(--br-10xs-4);
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .payment-methodgooglepay-icon {
      height: 24px;
      width: 36px;
      position: relative;
      border-radius: var(--br-10xs-4);
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .payment-methodamex-icon {
      height: 24px;
      width: 36px;
      position: relative;
      border-radius: var(--br-10xs-4);
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .payment-methodpaypal-icon {
      height: 24px;
      width: 36px;
      position: relative;
      border-radius: var(--br-10xs-4);
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .payment-methodvisa-parent {
      height: 24px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      z-index: 1;
    }
    .electro-all-rights {
      flex: 1;
      position: relative;
      line-height: 30px;
      display: inline-block;
      min-width: 192px;
      z-index: 1;
    }
    .footer-container {
      width: 718px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: 203px;
      max-width: 100%;
    }
    .huge-iconsocialsolidfaceboo {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .huge-iconsocialsolidinstagr {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      object-fit: cover;
      min-height: 24px;
    }
    .huge-iconsocialsolidtwitter {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .instagram-instances {
      height: 24px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-xl);
      z-index: 1;
    }
    .footer-container-parent {
      align-self: stretch;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: space-between;
      max-width: 100%;
      gap: var(--gap-xl);
    }
    .rectangle-parent {
      width: 1140px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-base);
      max-width: 100%;
    }
    .footer {
      width: 1440px;
      max-width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding: 30px var(--padding-xl) var(--padding-base);
      box-sizing: border-box;
      position: relative;
      gap: 64px;
      letter-spacing: normal;
      text-align: center;
      font-size: var(--body-1-regular-size);
      color: var(--white-500);
      font-family: var(--body-1-regular);
    }

    @media screen and (max-width: 1200px) {
      .footer {
        gap: 32px 64px;
      }
    }
    @media screen and (max-width: 1050px) {
      .frame-group {
        flex-wrap: wrap;
      }
  
      .footer-container-parent {
        flex-wrap: wrap;
      }
    }
    @media screen and (max-width: 750px) {
      .footer-container {
        flex-wrap: wrap;
        gap: 203px 101px;
      }
  
      .footer {
        gap: 16px 64px;
      }
    }
    @media screen and (max-width: 450px) {
      .footer-container {
        gap: 203px 51px;
      }
    }
</style>
