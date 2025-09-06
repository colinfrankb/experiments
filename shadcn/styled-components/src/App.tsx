import './App.css'
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from '@/components/app-sidebar'

function App() {

  return (
    <SidebarProvider>
      <AppSidebar />
      <SidebarTrigger />
    </SidebarProvider>
  )
}

export default App
