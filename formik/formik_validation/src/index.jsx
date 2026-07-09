import { createRoot } from "react-dom/client";

import SignupForm from "./App";

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(<SignupForm />);
