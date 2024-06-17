<template>
  <div>
    <b-modal id="register-modal" hide-footer hide-header body-class="login-container">
      <div>
        <h2 class="welcome-text">Create New Account</h2>
        <p class="login-description">Please enter details</p>
        <form class="login-form">
          <label for="name" class="input-label">Name</label>
          <b-form-input v-model="user_data.name" class="mb-2" id="name" type="text" placeholder="Name" size="lg"></b-form-input>
          <label for="email" class="input-label">Email Address</label>
          <b-form-input v-model="user_data.email" class="mb-2" id="email" type="email" placeholder="Email" size="lg"></b-form-input>
          <label for="password" class="input-label">Password</label>
          <b-form-input v-model="user_data.password" class="mb-2" id="password" type="password" placeholder="Password" size="lg"></b-form-input>
          <div class="form-options">
            <div class="remember-me">
              <b-form-checkbox class="mt-2" id="checkbox2">
                I agree to the Terms & Conditions
              </b-form-checkbox>
            </div>
          </div>
          <button type="button" @click="register_user" class="register-button">Register</button>
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
    <b-button v-b-modal.register-modal class="register-button-login w-100">Register</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_data: {
        name: "",
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        username: "",
      }
    }
  },
  methods: {
    async register_user() {
      this.user_data.username = this.user_data.email
      this.user_data.first_name = this.user_data.name
      this.user_data.last_name = this.user_data.name
      const res = await this.$axios.$post('/api/register/', this.user_data)
      if (res.status === 201) {
          console.log("here")
          this.$bvModal.hide('register-modal')
      }
    }
  }
}
</script>


<style scoped>
.register-button-login {
  padding: 0.9rem;
  border-radius: 10px;
  font: 16px/30px Montserrat, sans-serif;
  white-space: nowrap;
  cursor: pointer;
  margin-top: 0.8rem;
  border: 1px solid rgba(28, 78, 142, 1);
  color: #1c4e8e;
  background-color: white;

}

.register-button {
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

.register-button {
  margin-top: 2rem;
  padding: 0.9rem;
  border: none;
  border-radius: 10px;
  font: 16px/30px Montserrat, sans-serif;
  white-space: nowrap;
  cursor: pointer;
}

.register-button {
  background-color: #1c4e8e;
  color: white;
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