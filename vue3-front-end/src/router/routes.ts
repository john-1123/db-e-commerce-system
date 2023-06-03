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
    component: () => import('../views/Home.vue'),
    meta: {
      layout: 'Default',
    },
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue'),
    beforeEnter: loginGuard,
    meta: {
      layout: 'Default',
    },
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/auth/SignUp.vue'),
    meta: {
      layout: 'Default',
    }
  },
  {
    path: '/sign-in',
    name: 'SignIn',
    component: () => import('../views/auth/SignIn.vue'),
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
  },
  {
    path: '/market',
    name: 'Market',
    component: () => import('../views/Market.vue'),
    beforeEnter: loginGuard,
    meta: {
      layout: 'Default'
    }
  },
  {
    path: '/',
    name: 'redirect',
    redirect: '/home'
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
    component: () => import('../views/manage/product/ProductList.vue'),
    meta: {
      layout: 'Default'
    }
  },
  {
    path: '/manage/product/create',
    name: 'CreateProduct',
    component: () => import('../views/manage/product/CreateProduct.vue'),
    meta: {
      layout: 'Default'
    }
  }
];

export default routes;
