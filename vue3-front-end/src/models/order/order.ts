import { PaymentMode } from "../cart/payment-mode";
import { TransportMode } from "../cart/transport-mode";

export default interface Order {
  order_id: number;
  create_time: Date;
  consignee: string;
  shipping_address: string;
  payment_method: PaymentMode;
  mode_of_transport: TransportMode;
  state: string;
  items: string;
  quantities: string;
  cashs: string;
  cost: number;
}
