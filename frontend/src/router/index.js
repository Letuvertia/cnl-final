import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'
import UserView from '../views/UserView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/user',
      name: 'user',
      component: UserView,
      meta: { requiresAuth: true }
    },
  ]
})

const sessionTimeout = 30 * 60 * 1000; // 30 minutes

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('authToken'); // Check if the token exists
  const loginTime = localStorage.getItem('loginTime');
  const currentTime = new Date().getTime();

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (isAuthenticated && loginTime && (currentTime - loginTime) < sessionTimeout) {
      next();
    } else {
      localStorage.removeItem('authToken');
      localStorage.removeItem('loginTime');
      next('/login');
    }
  } else {
    next();
  }
});


export default router
