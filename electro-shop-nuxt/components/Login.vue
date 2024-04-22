<template>
  <div>
    <b-modal id="login-modal" hide-footer hide-header body-class="login-container">
      <div>
        <h2 class="welcome-text">Welcome 👋</h2>
        <p class="login-description">Please login here</p>
        <form class="login-form">
          <label for="email" class="input-label">Email Address</label>
          <input type="email" id="email" class="input-field" value="kristin.watson@example.com" />
          <label for="password" class="input-label">Password</label>
          <input type="password" id="password" class="input-field" value="••••••••••••••••••" />
          <div class="form-options">
            <div class="remember-me">
              <!-- need to add checkmark -->checkmark
              <span class="remember-me-text">Remember Me</span>
            </div>
            <a href="#" class="forgot-password">Forgot Password?</a>
          </div>
          <button type="submit" class="login-button">Login</button>
          <button type="button" class="register-button">Register</button>
        </form>
        <div class="separator">
          <hr class="separator-line" />
          <span class="separator-text">Or Login With</span>
          <hr class="separator-line" />
        </div>
        <button type="button" class="social-login google-login">
          <img src="/login/google.jpg" alt="google icon" class="social-icon" />
          <span class="social-text">Login with Google</span>
        </button>
        <button type="button" class="social-login apple-login">
          <img src="/login/apple.jpg" alt="apple icon" class="social-icon" />
          <span class="social-text">Login with Apple</span>
        </button>
      </div>
    </b-modal>
    <b-button v-b-modal.login-modal class="login-button-navbar">Login</b-button>
  </div>
</template>

<style scoped>
.login-button-navbar {
  padding: 0.7rem 1.4rem;
  border: none;
  border-radius: 10px;
  background-color: #1c4e8e;
  font-family: Montserrat, sans-serif;
}

.login-button {
  padding: 20px;
  border: none;
  border-radius: 10px;
  background-color: var(--Primary-500, #1c4e8e);
  color: var(--White-500, #fff);
  font: 400 16px/30px Montserrat, sans-serif;
  cursor: pointer;
}

.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 420px;
  padding: 20px;
  border: 1px solid rgba(165, 169, 172, 0.2);
  border-radius: 16px;
  background-color: var(--White-500, #fff);
  box-shadow: 0px 10px 40px -4px rgba(16, 24, 40, 0.02), 0px 8px 8px -4px rgba(16, 24, 40, 0.02);
  color: var(--Dark-500, #101316);
  font-weight: 400;
}

.welcome-text {
  font: 700 30px/140% Montserrat, sans-serif;
}

.login-description {
  color: var(--Gray-500, #a5a9ac);
  font: 16px/30px Montserrat, sans-serif;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.input-label {
  margin-top: 23px;
  font: 12px/167% Montserrat, sans-serif;
}

.input-field {
  margin-top: 8px;
  padding: 21px 16px;
  border: 1px solid rgba(28, 78, 142, 1);
  border-radius: 10px;
  font: 16px/187.5% Montserrat, sans-serif;
  white-space: nowrap;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 16px/30px Montserrat, sans-serif;
}

.checkbox-icon {
  width: 24px;
  height: 24px;
  object-fit: auto;
  object-position: center;
}

.forgot-password {
  font: 14px/24px Montserrat, sans-serif;
  text-align: right;
}

.login-button,
.register-button {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  padding: 13px 20px;
  border: none;
  border-radius: 10px;
  font: 16px/30px Montserrat, sans-serif;
  white-space: nowrap;
  cursor: pointer;
}

.login-button {
  background-color: var(--Primary-500, #1c4e8e);
  color: var(--White-500, #fff);
}

.register-button {
  margin-top: 10px;
  border: 1px solid rgba(28, 78, 142, 1);
  color: var(--Primary-500, #1c4e8e);
}

.separator {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 16px;
  gap: 8px;
  font-size: 14px;
  text-align: center;
  line-height: 24px;
}

.separator-line {
  flex: 1;
  height: 1px;
  background-color: var(--gray-gray-20, rgba(165, 169, 172, 0.2));
  border: none;
}

.separator-text {
  font-family: Montserrat, sans-serif;
}

.social-login {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 16px;
  padding: 13px 20px;
  border: 1px solid rgba(165, 169, 172, 0.2);
  border-radius: 10px;
  font: 16px/30px Montserrat, sans-serif;
  background-color: transparent;
  cursor: pointer;
}

.google-login {
  margin-top: 16px;
}

.apple-login {
  margin-top: 10px;
}

.social-icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}

.social-text {
  font-family: Montserrat, sans-serif;
}
</style>