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
    path: '/carts',
    name: 'Cart',
    component: () => import('../views/Cart.vue'),
    meta: {
      layout: 'Default'
    }
  },
  {
    path: '/orders',
    name: 'Order',
    component: () => import('../views/Order.vue'),
    meta: {
      layout: 'Default'
    }
  },
  {
    path: '/product/detail',
    name: 'ProductDetail',
    component: () => import('../views/ProductDetail.vue'),
    meta: {
      layout: 'Default'
    }
  },
  {
    path: '/manage/product',
    name: 'ManageProduct',
    component: () => import('../views/ManageProduct.vue'),
    meta: {
      layout: 'Default'
    }
  }
];

export default routes;
