import { RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "home" */ '../views/Home.vue'),
    meta: {
      layout: 'Default',
    },
    alias: '/home',
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import(/* webpackChunkName: "profile" */ '../views/Profile.vue'),
    meta: {
      layout: 'Default',
    },
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/SignUp.vue'),
    meta: {
      layout: 'Default',
    }
  },
  {
    path: '/sign-in',
    name: 'SignIn',
    component: () => import('../views/SignIn.vue'),
    meta: {
      layout: 'Default',
    }
  },
  {
    path: '/products',
    name: 'Proudct',
    component: () => import('../views/Products.vue'),
    meta: {
      layout: 'Default'
    }
  }
];

export default routes;
