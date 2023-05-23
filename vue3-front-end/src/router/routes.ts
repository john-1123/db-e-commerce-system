import { RouteRecordRaw } from 'vue-router';

function loginGuard() {
  if(sessionStorage.getItem('user')==null) {
    return { name: 'SignIn'}
  }
  return true
}

const routes: Array<RouteRecordRaw> = [
  {
    path: '/home',
    name: 'Home',
    component: () => import(/* webpackChunkName: "home" */ '../views/Home.vue'),
    meta: {
      layout: 'Default',
    },
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import(/* webpackChunkName: "profile" */ '../views/Profile.vue'),
    beforeEnter: loginGuard,
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
    beforeEnter: loginGuard,
    meta: {
      layout: 'Default'
    }
  },
  {
    path: '/orders',
    name: 'Order',
    component: () => import('../views/Order.vue'),
    beforeEnter: loginGuard,
    meta: {
      layout: 'Default'
    }
  }
];

export default routes;
