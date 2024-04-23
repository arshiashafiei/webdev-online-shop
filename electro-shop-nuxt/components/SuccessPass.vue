<template>
    <b-modal id="success-modal" hide-footer hide-header body-class="password-changed-container">
        <div class="success-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="4" y="7" width="16" height="14" rx="4" stroke="white" stroke-width="1.5" />
                <circle cx="12" cy="14" r="2" stroke="white" stroke-width="1.5" />
                <path d="M16 7C16 4.79086 14.2091 3 12 3C9.79086 3 8 4.79086 8 7" stroke="white" stroke-width="1.5" />
            </svg>
        </div>
        <h2 class="success-title">Password Changed Successfully</h2>
        <p class="success-description">Your password has been updated successfully</p>
        <button type="submit" class="back-to-login-button">Back to Login</button>
    </b-modal>
</template>

<style scoped>
.password-changed-container {
    max-width: 392px;
    padding: 20px;
    border: 1px solid rgba(165, 169, 172, 0.2);
    border-radius: 16px;
    background-color: var(--White-500, #fff);
    box-shadow: 0px 10px 40px -4px rgba(16, 24, 40, 0.02), 0px 8px 8px -4px rgba(16, 24, 40, 0.02);
    font-size: 16px;
    font-weight: 400;
    line-height: 30px;
    color: var(--Dark-500, #101316);
    display: flex;
    flex-direction: column;
}

.success-icon {
    width: 108px;
    height: 108px;
    margin: 0 auto;
    border-radius: 50%;
    background-color: var(--primary-primary-10, rgba(28, 78, 142, 0.1));
    object-fit: auto;
    object-position: center;
}

.success-title {
    margin-top: 20px;
    font: 700 24px/36px Montserrat, sans-serif;
    text-align: center;
}

.success-description {
    margin-top: 10px;
    font-family: Montserrat, sans-serif;
    text-align: center;
}

.back-to-login-button {
    margin-top: 30px;
    padding: 13px 20px;
    border-radius: 10px;
    background-color: var(--Primary-500, #1c4e8e);
    color: var(--White-500, #fff);
    font-family: Montserrat, sans-serif;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
</style>