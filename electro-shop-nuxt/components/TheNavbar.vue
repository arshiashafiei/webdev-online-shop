<template>
    <div>
        <b-navbar toggleable="lg" type="light">
            <b-navbar-brand href="#">
                <b-img class="logo" alt="Electro" src="/logo.svg" />
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-container>
                <b-row align-v="center">
                    <b-column>
                        <b-nav-item-dropdown class="border squared-right rounded-left" text="All" right>
                        <b-dropdown-item href="#">Cat1</b-dropdown-item>
                        <b-dropdown-item href="#">Cat2</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </b-column>

                    <b-column>
                        <b-nav-form>
                            <b-img class="logo" alt="Electro" src="/icons/search-icon.svg" />
                            <b-form-input type="search" class="squared-left squared-right" placeholder="Search"></b-form-input>
                            <b-button class="squared-left rounded-right button" type="submit">Search</b-button>
                        </b-nav-form>
                    </b-column>
                </b-row>
            </b-container>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <div class="d-flex">
                    <b-img class="icon m5" alt="search" src="/icons/search-icon.svg" />
                    <b-img class="icon m5" alt="heart" src="/icons/heart-icon.svg" />
                    <b-img class="icon m5" alt="cart" src="/icons/cart-icon.svg" />
                    <b-button class="button m5" href="#">Login</b-button>
                </div>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
</script>

<style scoped>
    .logo {
        align-self: stretch;
        height: 35px;
        position: relative;
        max-width: 100%;
        overflow: hidden;
        flex-shrink: 0;
        z-index: 1;
    }

    .icon {
        height: 24px;
        width: 24px;
        position: relative;
        overflow: hidden;
        flex-shrink: 0;
        min-height: 24px;
    }

    .squared-left {
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
    }

    .squared-right {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
    }

    .rounded-right {
        border-top-right-radius: 0.5rem;
        border-bottom-right-radius: 0.5rem;
    }

    .rounded-left {
        border-top-left-radius: 0.5rem;
        border-bottom-left-radius: 0.5rem;
    }

    .button {
        background-color: #1C4E8E;
        border-color: #1C4E8E;
        color: white;
    }

    .button:hover {
        background-color: darken(#1C4E8E, 10%);
        border-color: darken(#1C4E8E, 10%);
    }
</style>