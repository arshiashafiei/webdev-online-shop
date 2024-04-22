<template>
  <b-container fluid>
    <CartSidebar />
    <div class="header">
      <div class="header-content">
        <div class="header-top">
          <div class="logo-search">
            <img src="" alt="Company Logo" class="logo" />
            <div class="search-bar">
              <div class="search-dropdown">
                <div class="search-dropdown-text">
                  <span>All</span>
                  <img src="" alt="Dropdown Arrow" class="dropdown-arrow" />
                </div>
              </div>
              <div class="search-input">
                <img src="" alt="Search Icon" class="search-icon" />
                <span>Search</span>
              </div>
              <button class="search-button">Search</button>
            </div>
          </div>
          <div class="header-icons">
            <div class="icon-group">
              <img src="" alt="Heart Icon" class="icon" />
              <img src="" alt="User Icon" class="icon" />
              <div class="cart-icon" v-b-toggle.cart-sidebar>
                <div class="icon">
                  <svg
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M11 20.5C11 21.3284 10.3284 22 9.5 22C8.67157 22 8 21.3284 8 20.5C8 19.6716 8.67157 19 9.5 19C10.3284 19 11 19.6716 11 20.5Z"
                      stroke="#28303F"
                      stroke-width="1.5"
                    />
                    <path
                      d="M20 20.5C20 21.3284 19.3284 22 18.5 22C17.6716 22 17 21.3284 17 20.5C17 19.6716 17.6716 19 18.5 19C19.3284 19 20 19.6716 20 20.5Z"
                      stroke="#28303F"
                      stroke-width="1.5"
                    />
                    <path
                      d="M6 4H18C20.2091 4 22 5.79086 22 8V13C22 15.2091 20.2091 17 18 17H10C7.79086 17 6 15.2091 6 13V4ZM6 4C6 2.89543 5.10457 2 4 2H2M6 8H21.5"
                      stroke="#28303F"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                </div>
                <span class="cart-count">{{ $store.state.products_in_cart.length }}</span>
              </div>
            </div>
            <Login />
          </div>
        </div>
        <div class="header-bottom">
          <div class="category-dropdown">
            <div class="category-text">
              <img src="" alt="Category Icon" class="category-icon" />
              <span>All Categories</span>
              <img src="" alt="Dropdown Arrow" class="dropdown-arrow" />
            </div>
          </div>
          <nav class="main-nav">
            <a href="#" class="nav-link">Home</a>
            <div class="nav-link-group">
              <a href="#" class="nav-link">Shop</a>
              <img src="" alt="Dropdown Arrow" class="dropdown-arrow" />
            </div>
            <a href="#" class="nav-link">About Us</a>
            <a href="#" class="nav-link">Blog</a>
            <a href="#" class="nav-link">Contact Us</a>
          </nav>
        </div>
      </div>
    </div>
  </b-container>
</template>

<style scoped>
.header {
  background-color: var(--White-500, #fff);
  display: flex;
  justify-content: center;
  padding: 20px 60px 0;
}

@media (max-width: 991px) {
  .header {
    padding: 0 20px;
  }
}

.header-content {
  display: flex;
  flex-direction: column;
  max-width: 1440px;
  width: 100%;
}

@media (max-width: 991px) {
  .header-content {
    max-width: 100%;
  }
}

.header-top {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  width: 100%;
}

@media (max-width: 991px) {
  .header-top {
    flex-wrap: wrap;
  }
}

.logo-search {
  display: flex;
  align-items: center;
  gap: 20px;
  font-size: 16px;
  font-weight: 400;
  line-height: 30px;
}

@media (max-width: 991px) {
  .logo-search {
    flex-wrap: wrap;
  }
}

.logo {
  width: 179px;
  max-width: 100%;
  aspect-ratio: 5;
  object-fit: contain;
}

.search-bar {
  display: flex;
  flex: 1;
}

@media (max-width: 991px) {
  .search-bar {
    flex-wrap: wrap;
  }
}

.search-dropdown {
  display: flex;
  align-items: center;
  padding: 13px 16px;
  border: 1px solid rgba(165, 169, 172, 0.2);
  border-radius: 10px 0 0 10px;
  color: var(--Dark-500, #101316);
}

.search-dropdown-text {
  display: flex;
  align-items: center;
  gap: 10px;
}

.dropdown-arrow {
  width: 24px;
  aspect-ratio: 1;
  object-fit: contain;
}

.search-input {
  display: flex;
  align-items: center;
  padding: 13px 16px;
  border: 1px solid rgba(165, 169, 172, 0.2);
  color: var(--dark-dark-20, rgba(16, 19, 22, 0.2));
}

.search-icon {
  width: 24px;
  aspect-ratio: 1;
  object-fit: contain;
  margin-right: 10px;
}

.search-button {
  padding: 20px;
  border: none;
  border-radius: 0 10px 10px 0;
  background-color: var(--Primary-500, #1c4e8e);
  color: var(--White-500, #fff);
  font-family: Montserrat, sans-serif;
  cursor: pointer;
}

.header-icons {
  display: flex;
  align-items: center;
  gap: 20px;
  color: var(--White-500, #fff);
}

.icon-group {
  display: flex;
  align-items: center;
  gap: 20px;
  font-size: 11px;
  font-weight: 700;
  text-align: center;
  line-height: 145%;
}

.icon {
  object-fit: contain;
}

.cart-icon {
  position: relative;
  display: flex;
  align-items: flex-start;
  padding: 0 14px 13px;
  overflow: hidden;
}

.icon-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.cart-count {
  position: relative;
  display: flex;
  justify-content: center;
  padding: 2px 0;
  border-radius: 50%;
  background-color: var(--Primary-500, #1c4e8e);
  font-family: Montserrat, sans-serif;
}

.header-bottom {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: 30px;
  font-size: 16px;
  color: var(--Dark-500, #101316);
  font-weight: 400;
  line-height: 30px;
}

@media (max-width: 991px) {
  .header-bottom {
    flex-wrap: wrap;
  }
}

.category-dropdown {
  display: flex;
  align-items: center;
  padding: 10px 16px;
  border-radius: 5px 5px 0 0;
  background-color: var(--gray-gray-5, rgba(165, 169, 172, 0.05));
  flex: 1;
  width: fit-content;
}

.category-text {
  display: flex;
  align-items: center;
  gap: 10px;
}

.category-icon {
  width: 24px;
  aspect-ratio: 1;
  object-fit: contain;
  margin-right: 10px;
}

.main-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  flex: 1;
}

@media (max-width: 991px) {
  .main-nav {
    flex-wrap: wrap;
  }
}

.nav-link {
  font-family: Montserrat, sans-serif;
  text-decoration: none;
  color: inherit;
}

.nav-link-group {
  display: flex;
  align-items: center;
  gap: 10px;
}
</style>
