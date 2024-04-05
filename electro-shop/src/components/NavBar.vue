<template>
    <div class="header">
      <form class="frame-parent">
        <div class="input-container-parent">
          <div class="input-container">
            <img class="logo-text" loading="lazy" alt="" src="../assets/logo.svg" />
          </div>
          <div class="input-parent">
            <div class="input">
              <div class="text-parent">
                <div class="text">All</div>
                <img class="icon" alt="" src="../assets/arrow-down.svg" />
              </div>
            </div>
            <div class="input1">
              <div class="cart-item-preview">
                <img class="icon1" alt="" src="../assets/search.svg" />
                <input class="text1" placeholder="Search" type="text" />
              </div>
            </div>
            <button class="button">
              <div class="button1">Search</div>
            </button>
          </div>
        </div>
        <div class="input-group">
          <button class="input2">
            <div class="input-field-with-dropdown">
              <div class="icon-wrapper">
                <img class="icon2" alt="" src="../assets/menu-line-horizontal.png" />
              </div>
              <div class="text2">All Categories</div>
              <div class="icon-container">
                <img class="icon3" alt="" src="../assets/arrow-down.svg" />
              </div>
            </div>
          </button>
          <div class="nav-bar-container">
            <div class="home-parent">
              <div class="home">Home</div>
              <div class="shop-button">
                <div class="shop">Shop</div>
                <div class="search-icon">
                  <img
                    class="huge-iconarrowsoutlinedirec"
                    alt=""
                    src="../assets/arrow-down.svg"
                  />
                </div>
              </div>
              <div class="about-us">About Us</div>
              <div class="blog">Blog</div>
              <div class="contact-us">Contact Us</div>
            </div>
          </div>
        </div>
      </form>
      <div class="search-input-label-parent">
        <div class="search-input-label">
          <div class="search-button">
            <img
              class="huge-iconinterfacesolidsear"
              loading="lazy"
              alt=""
              src="../assets/search.svg"
            />
            <img
              class="huge-iconinterfacesolidsear1"
              loading="lazy"
              alt=""
              src="../assets/love.svg"
            />
            <div class="cart-item">
              <img
                class="huge-iconinterfacesolidsear2"
                loading="lazy"
                alt=""
                src="../assets/cart.svg"
              />
              <div class="cart-item1">
                <div class="header-button-container" />
                <b class="button-label">2</b>
              </div>
            </div>
          </div>
        </div>
        <button class="button2">
          <div class="button3">Login</div>
        </button>
      </div>
    </div>
  </template>

  <style scoped>
    .logo-icon {
      height: 58px;
      width: 58px;
      position: absolute;
      margin: 0 !important;
      top: calc(50% - 29px);
      left: 150px;
      overflow: hidden;
      flex-shrink: 0;
      object-fit: contain;
    }
    .logo-text {
      align-self: stretch;
      height: 35px;
      position: relative;
      max-width: 100%;
      overflow: hidden;
      flex-shrink: 0;
      z-index: 1;
    }
    .input-container {
      height: 42px;
      width: 178.5px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-end;
      padding: 0px 0px 7px;
      box-sizing: border-box;
    }
    .text {
      flex: 1;
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--dark-500);
      text-align: left;
      white-space: nowrap;
    }
    .icon {
      height: 24px;
      width: 24px;
      position: relative;
    }
    .text-parent {
      align-self: stretch;
      flex: 1;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-start;
      gap: var(--gap-3xs);
    }
    .input {
      align-self: stretch;
      width: 93px;
      border-radius: var(--br-3xs) 0px 0px var(--br-3xs);
      border-top: 1px solid var(--gray-gray-20);
      border-bottom: 1px solid var(--gray-gray-20);
      border-left: 1px solid var(--gray-gray-20);
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      padding: var(--padding-3xs) var(--padding-mini);
    }
    .icon1 {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .text1 {
      width: calc(100% - 24px);
      border: none;
      outline: none;
      font-family: var(--body-1-regular);
      font-size: var(--body-1-regular-size);
      background-color: transparent;
      height: 30px;
      flex: 1;
      position: relative;
      line-height: 30px;
      color: var(--dark-dark-20);
      text-align: left;
      display: inline-block;
      min-width: 169px;
      padding: 0;
    }
    .cart-item-preview {
      align-self: stretch;
      flex: 1;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-start;
      gap: var(--gap-3xs);
    }
    .input1 {
      align-self: stretch;
      flex: 1;
      border: 1px solid var(--gray-gray-20);
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      padding: var(--padding-3xs) var(--padding-mini);
      max-width: 100%;
    }
    .button1 {
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--white-500);
      text-align: left;
      display: inline-block;
      min-width: 56px;
      white-space: nowrap;
    }
    .button {
      cursor: pointer;
      border: none;
      padding: var(--padding-3xs) 21px;
      background-color: var(--primary-500);
      border-radius: 0px var(--br-3xs) var(--br-3xs) 0px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
    }
    .button:hover {
      background-color: var(--color-steelblue);
    }
    .input-parent {
      align-self: stretch;
      flex: 1;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      max-width: 100%;
    }
    .input-container-parent {
      width: 747px;
      flex: 1;
      display: flex;
      flex-direction: row;
      align-items: flex-end;
      justify-content: flex-start;
      gap: 30.5px;
      max-width: 100%;
    }
    .icon2 {
      width: 24px;
      height: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      object-fit: cover;
    }
    .icon-wrapper {
      height: 27px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-10xs) 0px 0px;
      box-sizing: border-box;
    }
    .text2 {
      flex: 1;
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--dark-500);
      text-align: left;
      white-space: nowrap;
    }
    .icon3 {
      width: 24px;
      height: 24px;
      position: relative;
    }
    .icon-container {
      height: 27px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-10xs) 0px 0px;
      box-sizing: border-box;
    }
    .input-field-with-dropdown {
      flex: 1;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
    }
    .input2 {
      cursor: pointer;
      border: none;
      padding: var(--padding-3xs) 16px;
      background-color: var(--gray-gray-5);
      width: 317px;
      border-radius: var(--br-8xs) var(--br-8xs) 0px 0px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      box-sizing: border-box;
      z-index: 1;
    }
    .home {
      width: 50px;
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--dark-500);
      text-align: center;
      display: inline-block;
      min-width: 50px;
      white-space: nowrap;
    }
    .shop {
      flex: 1;
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--dark-500);
      text-align: center;
      display: inline-block;
      min-width: 42px;
      white-space: nowrap;
    }
    .huge-iconarrowsoutlinedirec {
      width: 24px;
      height: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .search-icon {
      height: 27px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-10xs) 0px 0px;
      box-sizing: border-box;
    }
    .shop-button {
      width: 66px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
    }
    .about-us {
      width: 75px;
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--dark-500);
      text-align: center;
      display: inline-block;
      min-width: 75px;
      white-space: nowrap;
    }
    .blog {
      width: 38px;
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--dark-500);
      text-align: center;
      display: inline-block;
      min-width: 38px;
      white-space: nowrap;
    }
    .contact-us {
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--dark-500);
      text-align: center;
      display: inline-block;
      min-width: 89px;
      white-space: nowrap;
    }
    .home-parent {
      align-self: stretch;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: space-between;
      gap: var(--gap-xl);
    }
    .nav-bar-container {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-3xs) 0px 0px;
      box-sizing: border-box;
      max-width: 100%;
    }
    .input-group {
      align-self: stretch;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-11xl);
      max-width: 100%;
    }
    .frame-parent {
      margin: 0;
      height: 130px;
      width: 785px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-11xl);
      max-width: 100%;
    }
    .huge-iconinterfacesolidsear {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .huge-iconinterfacesolidsear1 {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      min-height: 24px;
    }
    .huge-iconinterfacesolidsear2 {
      height: 24px;
      width: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .header-button-container {
      position: absolute;
      top: 0px;
      left: 0px;
      border-radius: 50%;
      background-color: var(--primary-500);
      width: 100%;
      height: 100%;
    }
    .button-label {
      position: absolute;
      top: 1px;
      left: 5px;
      line-height: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 7px;
      height: 15px;
      min-width: 7px;
      z-index: 1;
    }
    .cart-item1 {
      height: 16px;
      width: 16px;
      position: absolute;
      margin: 0 !important;
      top: -5px;
      right: -6px;
      z-index: 1;
    }
    .cart-item {
      align-self: stretch;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      position: relative;
    }
    .search-button {
      flex: 1;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-xl);
    }
    .search-input-label {
      height: 37px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: 13px 0px 0px;
      box-sizing: border-box;
    }
    .button3 {
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--white-500);
      text-align: left;
      display: inline-block;
      min-width: 46px;
      white-space: nowrap;
    }
    .button2 {
      cursor: pointer;
      border: none;
      padding: var(--padding-3xs) 26px;
      background-color: var(--primary-500);
      border-radius: var(--br-3xs);
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
    }
    .button2:hover {
      background-color: var(--color-steelblue);
    }
    .search-input-label-parent {
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-11xl);
    }
    .header {
      width: 1440px;
      background-color: var(--white-500);
      max-width: 100%;
      overflow: hidden;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: space-between;
      padding: var(--padding-xl) 150px 0px;
      box-sizing: border-box;
      position: sticky;
      top: 0;
      z-index: 99;
      letter-spacing: normal;
      gap: var(--gap-xl);
      text-align: center;
      font-size: var(--label-bold-size);
      color: var(--white-500);
      font-family: var(--body-1-regular);
    }
  
    @media screen and (max-width: 1025px) {
      .home-parent {
        display: none;
      }
    }
    @media screen and (max-width: 975px) {
      .input-container-parent {
        gap: 30.5px 15px;
      }
    }
    @media screen and (max-width: 725px) {
      .header {
        padding-left: var(--padding-56xl);
        padding-right: var(--padding-56xl);
        box-sizing: border-box;
      }
    }
    @media screen and (max-width: 450px) {
      .header {
        padding-left: var(--padding-xl);
        padding-right: var(--padding-xl);
        box-sizing: border-box;
      }
    }
  </style>
  
  <script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "NavBar",
  });
  </script>
