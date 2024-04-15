<template>
    <b-container fluid>
        <div class="footer-top">
            <div class="footer-content">
                <div class="footer-info">
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
                            <img src="/icons/location-icon.svg" alt="Location icon" class="icon" />
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
                </div>
            </div>
        </div>
    </b-container>
</template>
  
<style scoped>
    .footer {
    display: flex;
    justify-content: center;
    }

    .footer-top {
    background-color: #1c4e8e;
    width: 100%;
    padding: 26px 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    }

    @media (max-width: 991px) {
    .footer-top {
        padding: 0 20px;
    }
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

    @media (max-width: 991px) {
    .footer-info {
        flex-wrap: wrap;
    }
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
</style>