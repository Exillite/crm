<template>
    <v-container class="fill-height d-flex flex-column justify-space-between" fluid>
        <v-row align="center" justify="center" class="flex-grow-1">
            <v-col cols="12" sm="8" md="4">
                <v-card outlined>
                    <v-card-title class="text-center">Регистрация</v-card-title>
                    <v-card-text>
                        <v-form ref="form" v-model="valid" lazy-validation>
                            <v-text-field v-model="login" label="Логин" outlined :rules="loginRules"
                                required></v-text-field>
                            <v-text-field v-model="contact" label="Email или Телефон" outlined :rules="contactRules"
                                required></v-text-field>
                            <v-text-field v-model="password" label="Пароль" type="password" outlined
                                :rules="passwordRules" required></v-text-field>
                            <v-text-field v-model="confirmPassword" label="Повторите пароль" type="password" outlined
                                :rules="confirmPasswordRules" required></v-text-field>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="primary" block @click="register" :disabled="!valid">Зарегистрироваться</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: 'Register',
    data() {
        return {
            valid: false,
            login: '',
            contact: '',
            password: '',
            confirmPassword: '',
            loginRules: [
                v => !!v || 'Введите логин',
                v => (v && v.length >= 3) || 'Логин должен содержать минимум 3 символа'
            ],
            contactRules: [
                v => !!v || 'Введите Email или Телефон',
            ],
            passwordRules: [
                v => !!v || 'Введите пароль',
                v => (v && v.length >= 8) || 'Пароль должен содержать минимум 8 символов'
            ],
            confirmPasswordRules: [
                v => !!v || 'Повторите пароль',
                v => v === this.password || 'Пароли должны совпадать'
            ]
        }
    },
    methods: {
        register() {
            if (this.$refs.form.validate()) {
                // Handle successful registration logic
                alert('Registration successful!')
            }
        },
    }
}
</script>

<style scoped>

.v-row {
    width: 100%;
}
</style>