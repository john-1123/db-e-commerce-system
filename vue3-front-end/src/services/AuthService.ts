import http from "../http-common";
import Login from "../models/user/login";
import SignUp from "../models/user/signup";

class AuthService {
  signup(data: SignUp): Promise<any> {
    return http.post("/signup", data);
  }

  login(data: Login): Promise<any> {
    return http.post(`/login`, data);
  }
}
export default new AuthService();
