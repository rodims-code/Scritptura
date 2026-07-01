<script>
	let { children } = $props();
	let isDrawerOpen = $state(true); // Control desktop collapse state
</script>

<!-- 
  Responsive collapsible Icon-only drawer sidebar. 
  On mobile: uses standard drawer toggle
  On desktop: uses is-drawer-open / is-drawer-close to shrink to icon-only 
-->
<div class="drawer lg:drawer-open">
	<input id="dashboard-drawer" type="checkbox" class="drawer-toggle" />

	<div class="drawer-content flex flex-col h-screen">
		<!-- Navbar -->
		<div class="navbar bg-base-100 border-b border-base-200 w-full">
			<div class="flex-none lg:hidden">
				<label for="dashboard-drawer" aria-label="open sidebar" class="btn btn-square btn-ghost">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-6 w-6 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
				</label>
			</div>
			<div class="flex-none hidden lg:block">
				<!-- Desktop toggle for icon-only mode -->
				<button aria-label="toggle sidebar" class="btn btn-square btn-ghost" onclick={() => (isDrawerOpen = !isDrawerOpen)}>
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-6 w-6 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
				</button>
			</div>
			<div class="flex-1 px-2 mx-2 text-xl font-bold">Dashboard</div>
			<div class="flex-none">
				<div class="dropdown dropdown-end">
					<div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
						<div class="w-10 rounded-full">
							<img alt="User avatar" src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
						</div>
					</div>
					<ul tabindex="0" class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
						<li><a>Profile</a></li>
						<li><a>Settings</a></li>
						<li><a>Logout</a></li>
					</ul>
				</div>
			</div>
		</div>

		<!-- Page Content -->
		<main class="flex-1 overflow-y-auto p-4 bg-base-200/50">
			{@render children()}
		</main>
	</div>

	<div class="drawer-side z-20">
		<label for="dashboard-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
		<!-- Sidebar uses is-drawer-open and is-drawer-close based on state -->
		<aside class="bg-base-100 min-h-screen text-base-content border-r border-base-200 transition-all duration-300 ease-in-out flex flex-col {isDrawerOpen ? 'w-72 is-drawer-open' : 'w-20 is-drawer-close'}">
			
			<div class="h-16 flex items-center justify-center border-b border-base-200">
				<div class="font-bold text-2xl text-primary transition-all duration-300 whitespace-nowrap overflow-hidden">
					{#if isDrawerOpen}
						Scriptura
					{:else}
						S
					{/if}
				</div>
			</div>

			<ul class="menu p-4 w-full gap-2 flex-1 flex-nowrap overflow-x-hidden">
				<li>
					<a href="/dashboard" class="flex items-center gap-4 tooltip-right {isDrawerOpen ? '' : 'justify-center px-0'}" data-tip={!isDrawerOpen ? "Home" : ""}>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>
						{#if isDrawerOpen}
							<span class="whitespace-nowrap transition-opacity duration-300">Home</span>
						{/if}
					</a>
				</li>
				<li>
					<a href="/dashboard/projects" class="flex items-center gap-4 tooltip-right {isDrawerOpen ? '' : 'justify-center px-0'}" data-tip={!isDrawerOpen ? "Projects" : ""}>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" /></svg>
						{#if isDrawerOpen}
							<span class="whitespace-nowrap transition-opacity duration-300">Projects</span>
						{/if}
					</a>
				</li>
				<li>
					<a href="/dashboard/analytics" class="flex items-center gap-4 tooltip-right {isDrawerOpen ? '' : 'justify-center px-0'}" data-tip={!isDrawerOpen ? "Analytics" : ""}>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
						{#if isDrawerOpen}
							<span class="whitespace-nowrap transition-opacity duration-300">Analytics</span>
						{/if}
					</a>
				</li>
				<li>
					<a href="/dashboard/settings" class="flex items-center gap-4 tooltip-right {isDrawerOpen ? '' : 'justify-center px-0'}" data-tip={!isDrawerOpen ? "Settings" : ""}>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
						{#if isDrawerOpen}
							<span class="whitespace-nowrap transition-opacity duration-300">Settings</span>
						{/if}
					</a>
				</li>
			</ul>

			<!-- Footer part of sidebar -->
			<div class="p-4 border-t border-base-200">
				<a href="/" class="btn btn-ghost w-full flex items-center justify-center gap-4 {isDrawerOpen ? 'justify-start' : 'px-0 tooltip-right'}" data-tip={!isDrawerOpen ? "Logout" : ""}>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" /></svg>
					{#if isDrawerOpen}
						<span class="whitespace-nowrap">Logout</span>
					{/if}
				</a>
			</div>
		</aside>
	</div>
</div>
