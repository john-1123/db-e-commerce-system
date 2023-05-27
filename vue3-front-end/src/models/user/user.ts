// export default interface User {
//   user_id: number;
//   username: string;
//   email: string;
//   password: string;
//   address: string;
//   phone: string;
// }

export default class User {
  user_id?: number;
  username: string;
  email: string;
  password: string;
  address: string;
  phone: string;

  constructor(
    username: string,
    email: string,
    password: string,
    address: string,
    phone: string,
    user_id?: number
  ) {
    if (user_id) {
      this.user_id = user_id;
    }
    this.username = username;
    this.email = email;
    this.password = password;
    this.address = address;
    this.phone = phone;
  }
}
