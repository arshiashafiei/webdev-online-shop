<template>
  <div>
    <Otp />
    <b-modal id="login-modal" hide-footer hide-header body-class="login-container">
      <div>
        <h2 class="welcome-text">Welcome 👋</h2>
        <p class="login-description">Please login here</p>
        <form class="login-form">
          <label for="email" class="input-label">Email Address</label>
          <b-form-input v-model="username" class="mb-2" id="email" type="email" placeholder="Email" size="md"></b-form-input>
          <label for="password" class="input-label">Password</label>
          <b-form-input v-model="password" class="mb-2" id="password" type="password" placeholder="Password" size="md"></b-form-input>
          <div class="form-options">
            <div class="remember-me">
              <b-form-checkbox class="mt-2" id="checkbox">
                Remember Me
              </b-form-checkbox>
            </div>
            <a href="#" class="forgot-password mt-2" v-b-modal.otp-modal>Forgot Password?</a>
          </div>
          <div class="d-flex flex-column">
            <button type="button" @click="login" class="login-button">Login</button>
            <Register />
          </div>
        </form>
        <div class="separator">
          <hr class="separator-line" />
          <span class="separator-text">Or Login With</span>
          <hr class="separator-line" />
        </div>
        <div class="d-flex flex-column">
          <button type="button" class="social-login google-login">
            <img src="/login/google.jpg" alt="google icon" class="social-icon" />
            <span class="social-text">Login with Google</span>
          </button>
          <button type="button" class="social-login apple-login">
            <img src="/login/apple.jpg" alt="apple icon" class="social-icon" />
            <span class="social-text">Login with Apple</span>
          </button>
        </div>
      </div>
    </b-modal>
    <b-button v-if="!$store.state.isAuthenticated" v-b-modal.login-modal class="login-button-navbar">Login</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    async login() {
      try {
        const res = await this.$axios.post('/api/login/', {
          username: this.username,
          password: this.password
        });
        if (res.status === 200) {
          this.$store.dispatch('checkAuth')
          this.$bvModal.hide('login-modal')
        }
      } catch (error) {
        console.error('Authentication error:', error);
      }
    },
  }
}
</script>

<style scoped>
.login-button-navbar {
  padding: 0.7rem 1.4rem;
  border: none;
  border-radius: 10px;
  background-color: #1c4e8e;
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
  border-radius: 2rem;
  background-color: white;
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
  font: 12px/167% Montserrat, sans-serif;
  margin-bottom: 0.2rem;
}

.input-field {
  margin-bottom: 1rem;
  padding: 1rem;
  border: 1px solid rgba(28, 78, 142, 1);
  border-radius: 10px;
  font: 16px/187.5% Montserrat, sans-serif;
  white-space: nowrap;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.remember-me {
  font: Montserrat, sans-serif;
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
  color: #101316;
}

.login-button,
.register-button {
  margin-top: 2rem;
  padding: 0.9rem;
  border: none;
  border-radius: 10px;
  font: 16px/30px Montserrat, sans-serif;
  white-space: nowrap;
  cursor: pointer;
}

.login-button {
  background-color: #1c4e8e;
  color: white;
}

.register-button {
  margin-top: 0.8rem;
  border: 1px solid rgba(28, 78, 142, 1);
  color: #1c4e8e;
  background-color: white;
}

.separator {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 1rem;
  gap: 0.5rem;
  text-align: center;
}

.separator-line {
  flex: 1;
  height: 1px;
  background-color: var(--gray-gray-20, rgba(165, 169, 172, 0.2));
  border: none;
}

.social-login {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
  border: 1px solid rgba(165, 169, 172, 0.2);
  border-radius: 10px;
  font: 16px/30px Montserrat, sans-serif;
  background-color: transparent;
  cursor: pointer;
}

.google-login {
  margin-top: 1rem;
}

.apple-login {
  margin-top: 0.6rem;
}

.social-icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}
</style>