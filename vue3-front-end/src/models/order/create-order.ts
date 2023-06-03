export default interface CreateOrder {
  member_id: number;
  market_id: number;
  state: string;
  shipping_address: string;
  consignee: string;
  payment_method: string;
  mode_of_transport: string;
}
