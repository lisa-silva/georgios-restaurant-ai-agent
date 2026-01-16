import { Toaster } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import NotFound from "@/pages/NotFound";
import { Route, Switch } from "wouter";
import ErrorBoundary from "./components/ErrorBoundary";
import { ThemeProvider } from "./contexts/ThemeContext";
import DashboardLayout from "./components/DashboardLayout";
import Home from "./pages/Home";
import VoiceOrders from "./pages/VoiceOrders";
import OrderManagement from "./pages/OrderManagement";
import Inventory from "./pages/Inventory";
import CustomerChat from "./pages/CustomerChat";
import Loyalty from "./pages/Loyalty";
import Analytics from "./pages/Analytics";
import MenuManagement from "./pages/MenuManagement";

function Router() {
  return (
    <DashboardLayout>
      <Switch>
        <Route path="/" component={Home} />
        <Route path="/voice-orders" component={VoiceOrders} />
        <Route path="/orders" component={OrderManagement} />
        <Route path="/inventory" component={Inventory} />
        <Route path="/chat" component={CustomerChat} />
        <Route path="/loyalty" component={Loyalty} />
        <Route path="/analytics" component={Analytics} />
        <Route path="/menu" component={MenuManagement} />
        <Route path="/404" component={NotFound} />
        <Route component={NotFound} />
      </Switch>
    </DashboardLayout>
  );
}

function App() {
  return (
    <ErrorBoundary>
      <ThemeProvider defaultTheme="light">
        <TooltipProvider>
          <Toaster />
          <Router />
        </TooltipProvider>
      </ThemeProvider>
    </ErrorBoundary>
  );
}

export default App;
