<script>
	import { page } from '$app/stores';
	let { children } = $props();
</script>

<!-- The main background uses base-200 to contrast with the base-100 blocks -->
<div class="h-screen w-full bg-base-200 p-4 md:p-6 font-sans text-base-content overflow-hidden flex gap-4 md:gap-6">
	
	<!-- Sidebar Block (Floating, Full height) -->
	<aside class="hidden md:flex w-[260px] flex-col justify-between rounded-[2rem] bg-base-100 shadow-sm overflow-hidden py-6">
		<div class="flex-1 overflow-y-auto no-scrollbar px-6">
			<!-- Logo -->
			<div class="mb-10 flex items-center gap-3">
				<div class="flex h-10 w-10 items-center justify-center rounded-xl bg-primary text-primary-content">
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
						<path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25zM12.75 6a.75.75 0 00-1.5 0v6c0 .414.336.75.75.75h4.5a.75.75 0 000-1.5h-3.75V6z" clip-rule="evenodd" />
					</svg>
				</div>
				<span class="text-2xl font-bold tracking-tight">Scriptura</span>
			</div>

			<!-- MENU Section -->
			<div class="mb-4 text-xs font-bold tracking-wider text-base-content/50 uppercase">Menu</div>
			<ul class="menu menu-md p-0 mb-8 space-y-2">
				<!-- Active Item with left border indicator -->
				<li class="relative">
					<div class="absolute -left-6 top-0 bottom-0 w-1.5 rounded-r-lg bg-primary"></div>
					<a href="/dashboard" class="flex gap-3 bg-transparent hover:bg-base-200 text-primary font-bold active:bg-base-200">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
							<path stroke-linecap="round" stroke-linejoin="round" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
						</svg>
						Dashboard
					</a>
				</li>
				
				<!-- Inactive Items -->
				<li>
					<a href="/dashboard/tasks" class="flex gap-3 text-base-content/70 hover:text-base-content">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
						</svg>
						Tasks
						<span class="badge badge-primary badge-sm ml-auto font-bold">12+</span>
					</a>
				</li>

				<li>
					<a href="/dashboard/calendar" class="flex gap-3 text-base-content/70 hover:text-base-content">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
						</svg>
						Calendar
					</a>
				</li>

				<li>
					<a href="/dashboard/analytics" class="flex gap-3 text-base-content/70 hover:text-base-content">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
						</svg>
						Analytics
					</a>
				</li>

				<li>
					<a href="/dashboard/team" class="flex gap-3 text-base-content/70 hover:text-base-content">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
						</svg>
						Team
					</a>
				</li>
			</ul>
		</div>

		<!-- GENERAL Section (Moved to the bottom) -->
		<div class="mt-auto px-6 pt-4">
			<div class="mb-4 text-xs font-bold tracking-wider text-base-content/50 uppercase">General</div>
			<ul class="menu menu-md p-0 space-y-2">
				<li>
					<a href="/dashboard/settings" class="flex gap-3 text-base-content/70 hover:text-base-content">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
							<path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
						</svg>
						Settings
					</a>
				</li>
				<li>
					<a href="/dashboard/help" class="flex gap-3 text-base-content/70 hover:text-base-content">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
						</svg>
						Help
					</a>
				</li>
				<li>
					<a href="/auth/login" class="flex gap-3 text-base-content/70 hover:text-error hover:bg-error/10">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
						</svg>
						Logout
					</a>
				</li>
			</ul>
		</div>
	</aside>

	<!-- Right Side Container (Topbar + Content) -->
	<div class="flex flex-1 flex-col gap-4 md:gap-6 overflow-hidden">
		
		<!-- Topbar Block (Floating) -->
		<header class="flex h-[88px] shrink-0 items-center justify-between rounded-[2rem] bg-base-100 px-6 md:px-10 shadow-sm">
			
			<!-- Mobile Menu Button (Visible only on small screens) -->
			<div class="md:hidden flex-none">
				<button class="btn btn-square btn-ghost">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-6 h-6 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
				</button>
			</div>

			<!-- Search -->
			<div class="relative w-full max-w-md hidden sm:block">
				<svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-base-content/40" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
					<path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
				</svg>
				<input type="text" placeholder="Search task" class="input bg-base-200/50 w-full rounded-2xl pl-12 pr-14 focus:bg-base-200 transition-colors border-none outline-none" />
				<div class="absolute right-3 top-1/2 -translate-y-1/2 rounded-lg bg-base-100 px-2 py-1 text-xs font-bold text-base-content/40 shadow-sm border border-base-200">
					⌘F
				</div>
			</div>

			<!-- Right Actions -->
			<div class="flex items-center gap-2 md:gap-6 ml-auto">
				<!-- Message Icon -->
				<button class="btn btn-circle btn-ghost text-base-content/60">
					<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
						<path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
					</svg>
				</button>

				<!-- Notification Icon -->
				<button class="btn btn-circle btn-ghost text-base-content/60 relative">
					<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
						<path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
					</svg>
					<span class="absolute right-2 top-2 h-2.5 w-2.5 rounded-full bg-error border-2 border-base-100"></span>
				</button>

				<!-- User Profile -->
				<div class="dropdown dropdown-end">
					<button tabindex="0" class="flex items-center gap-3 pl-2 btn btn-ghost h-auto hover:bg-transparent px-2">
						<div class="avatar">
							<div class="w-10 rounded-full border-2 border-base-100 shadow-sm">
								<img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" alt="Avatar" />
							</div>
						</div>
						<div class="hidden text-left sm:block">
							<div class="text-sm font-bold text-base-content">Utilisateur</div>
							<div class="text-xs font-medium text-base-content/50">user@email.com</div>
						</div>
					</button>
					<ul tabindex="0" class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52 z-[1] mt-4 border border-base-200">
						<li><a>Profil</a></li>
						<li><a>Paramètres</a></li>
						<li class="text-error"><a>Déconnexion</a></li>
					</ul>
				</div>
			</div>
		</header>

		<!-- Main Content Block (Floating) -->
		<main class="flex-1 overflow-y-auto rounded-[2rem] bg-base-100 p-6 md:p-10 shadow-sm no-scrollbar">
			{@render children()}
		</main>

	</div>
</div>

<style>
	/* Hide scrollbar for Chrome, Safari and Opera */
	.no-scrollbar::-webkit-scrollbar {
		display: none;
	}
	/* Hide scrollbar for IE, Edge and Firefox */
	.no-scrollbar {
		-ms-overflow-style: none;  /* IE and Edge */
		scrollbar-width: none;  /* Firefox */
	}
</style>
