<template>
    <div>
        <SuccessPass />
        <b-modal id="otp-modal" hide-footer hide-header body-class="otp-container">
            <h2 class="otp-title">Enter OTP</h2>
            <p class="otp-description">
                We have share a code of your registered email address kristin.watson@example.com
            </p>
            <form class="otp-form">
                <div class="otp-input-group">
                    <input type="text" class="otp-input" maxlength="1" aria-label="OTP digit 1" />
                    <input type="text" class="otp-input" maxlength="1" aria-label="OTP digit 2" />
                    <input type="text" class="otp-input" maxlength="1" aria-label="OTP digit 3" />
                    <input type="text" class="otp-input" maxlength="1" aria-label="OTP digit 4" />
                    <input type="text" class="otp-input" maxlength="1" aria-label="OTP digit 5" />
                </div>
                <button type="button" class="otp-submit-btn" v-b-modal.success-modal>Send OTP</button>
            </form>
        </b-modal>
    </div>
</template>

<style scoped>
.otp-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-width: 420px;
    padding: 20px;
    font-size: 16px;
    font-weight: 700;
    line-height: 30px;
    color: var(--Dark-500, #101316);
    background-color: var(--White-500, #fff);
    border: 1px solid rgba(165, 169, 172, 0.2);
    border-radius: 16px;
    box-shadow: 0px 10px 40px -4px rgba(16, 24, 40, 0.02), 0px 8px 8px -4px rgba(16, 24, 40, 0.02);
}

.otp-title {
    font: 30px/140% Montserrat, sans-serif;
}

.otp-description {
    margin-top: 5px;
    color: var(--Gray-500, #a5a9ac);
    font-weight: 400;
}

.otp-form {
    margin-top: 16px;
}

.otp-input-group {
    display: flex;
    gap: 20px;
    font-size: 24px;
    text-align: center;
    line-height: 150%;
    justify-content: center;
}

.otp-input {
    width: 60px;
    height: 60px;
    padding: 12px;
    border: 1px solid rgba(28, 78, 142, 1);
    border-radius: 10px;
    text-align: center;
}

.otp-submit-btn {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 30px;
    padding: 13px 20px;
    font-weight: 400;
    color: var(--White-500, #fff);
    background-color: var(--Primary-500, #1c4e8e);
    border: none;
    border-radius: 10px;
    cursor: pointer;
}
</style>