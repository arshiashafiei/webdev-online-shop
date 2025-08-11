<template>
  <b-container>
    <CartSidebar />
    <div class="header-top my-3">
      <div class="logo-search">
        <b-img src="/logo.svg" alt="Company Logo" class="logo" />
        <div class="search-bar">
          <b-dropdown variant="bg-transparent" class="search-dropdown" split text="All">
            <b-dropdown-item href="#">An item</b-dropdown-item>
            <b-dropdown-item href="#">Another item</b-dropdown-item>
          </b-dropdown>
          <div class="search-input">
            <img src="/icons/search-icon.svg" alt="Search Icon" class="search-icon" />
            <b-form-input class="search-input-inside" type="search" placeholder="Search"></b-form-input>
          </div>
          <b-button class="search-button">Search</b-button>
        </div>
      </div>
      <div class="header-icons">
        <div class="icon-group mr-3">
          <img src="/icons/search-icon.svg" alt="Heart Icon" class="icon" />
          <img src="/icons/heart-icon.svg" alt="User Icon" class="icon" />
          <div class="cart-icon" v-b-toggle.cart-sidebar>
            <div class="icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M11 20.5C11 21.3284 10.3284 22 9.5 22C8.67157 22 8 21.3284 8 20.5C8 19.6716 8.67157 19 9.5 19C10.3284 19 11 19.6716 11 20.5Z"
                  stroke="#28303F" stroke-width="1.5" />
                <path
                  d="M20 20.5C20 21.3284 19.3284 22 18.5 22C17.6716 22 17 21.3284 17 20.5C17 19.6716 17.6716 19 18.5 19C19.3284 19 20 19.6716 20 20.5Z"
                  stroke="#28303F" stroke-width="1.5" />
                <path
                  d="M6 4H18C20.2091 4 22 5.79086 22 8V13C22 15.2091 20.2091 17 18 17H10C7.79086 17 6 15.2091 6 13V4ZM6 4C6 2.89543 5.10457 2 4 2H2M6 8H21.5"
                  stroke="#28303F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
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
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd"
              d="M6.25 8C6.25 7.58579 6.58579 7.25 7 7.25H17C17.4142 7.25 17.75 7.58579 17.75 8C17.75 8.41421 17.4142 8.75 17 8.75H7C6.58579 8.75 6.25 8.41421 6.25 8ZM6.25 12C6.25 11.5858 6.58579 11.25 7 11.25H17C17.4142 11.25 17.75 11.5858 17.75 12C17.75 12.4142 17.4142 12.75 17 12.75H7C6.58579 12.75 6.25 12.4142 6.25 12ZM7 15.25C6.58579 15.25 6.25 15.5858 6.25 16C6.25 16.4142 6.58579 16.75 7 16.75H17C17.4142 16.75 17.75 16.4142 17.75 16C17.75 15.5858 17.4142 15.25 17 15.25H7Z"
              fill="#101316" />
          </svg>
          <b-dropdown variant="bg-transparent" split text="All Categories">
            <b-dropdown-item href="#">An item</b-dropdown-item>
            <b-dropdown-item href="#">Another item</b-dropdown-item>
          </b-dropdown>
        </div>
      </div>
      <nav class="main-nav">
        <a href="#" class="nav-link">Home</a>
        <div class="nav-link-group">
          <b-dropdown variant="bg-transparent" split text="Shop">
            <b-dropdown-item href="#">An item</b-dropdown-item>
            <b-dropdown-item href="#">Another item</b-dropdown-item>
          </b-dropdown>
        </div>
        <a href="#" class="nav-link">About Us</a>
        <a href="#" class="nav-link">Blog</a>
        <a href="#" class="nav-link">Contact Us</a>
      </nav>
    </div>
  </b-container>
</template>

<style scoped>
.logo {
  width: 179px;
  max-width: 100%;
  object-fit: contain;
}

.header-top {
  display: flex;
  justify-content: space-between;
  gap: 20px;
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
}

@media (max-width: 991px) {
  .logo-search {
    flex-wrap: wrap;
  }
}

.search-bar {
  display: flex;
}

.search-dropdown {
  border: 1px solid rgba(165, 169, 172, 0.2);
  border-radius: 10px 0 0 10px;
}

.search-input {
  display: flex;
  align-items: center;
  padding: 0px 1rem;
  border: 1px solid rgba(165, 169, 172, 0.2);
  color: rgba(16, 19, 22, 0.2);
}

.search-input-inside {
  border: 0;
}

.search-icon {
  width: 24px;
  margin-right: 10px;
}

.search-button {
  padding: 0.7rem 1.4rem;
  border: none;
  border-radius: 0 10px 10px 0;
  background-color: #1c4e8e;
}

.header-icons {
  display: flex;
  align-items: center;
  gap: 20px;
  color: white;
}

.icon-group {
  display: flex;
  align-items: center;
  gap: 20px;
  font-size: 11px;
  font-weight: 700;
}

.cart-icon {
  position: relative;
  display: flex;
  align-items: flex-start;
}

.icon-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.cart-count {
  position: absolute;
  display: flex;
  justify-content: center;
  padding: 2px 0;
  border-radius: 50%;
  background-color: var(--Primary-500, #1c4e8e);
  width: 20px;
  height: 20px;
  top: -8px;
  right: -10px;
}

.header-bottom {
  display: flex;
  margin-top: 1.5rem;
}

@media (max-width: 991px) {
  .header-bottom {
    flex-wrap: wrap;
  }
}

.category-dropdown {
  display: flex;
  padding: 5px 1rem;
  border-radius: 5px 5px 0 0;
  background-color: rgba(165, 169, 172, 0.1);
}

.main-nav {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-left: 1rem;
}

@media (max-width: 991px) {
  .main-nav {
    flex-wrap: wrap;
  }
}

.nav-link {
  color: inherit;
}
</style>
