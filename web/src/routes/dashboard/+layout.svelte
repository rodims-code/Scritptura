<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { fetchCurrentUser } from '$lib/apiUser.js';

	let { children } = $props();
	
	let user = $state(null);
	let loading = $state(true);

	onMount(async () => {
		const u = await fetchCurrentUser();
		if (!u) {
			goto('/auth/login');
		} else {
			user = u;
		}
		loading = false;
	});

	const menus = {
		STUDENT: [
			{ name: 'Dashboard', href: '/dashboard/student', icon: '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>' },
			{ name: 'Mes Cours', href: '/cursus', icon: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>' },
			{ name: 'Mon Relevé de Notes', href: '/grades', icon: '<path d="M21.42 10.922a2 2 0 0 1-.019 3.837l-8.5 4.354a2 2 0 0 1-1.802 0l-8.5-4.354a2 2 0 0 1-.019-3.837l8.5-4.473a2 2 0 0 1 1.84 0l8.5 4.473ZM14 14.5v3.424a2 2 0 0 1-1.042 1.758l-2 1a2 2 0 0 1-1.916 0l-2-1A2 2 0 0 1 6 17.924V14.5"/><path d="M6 11v5"/>' },
			{ name: 'Mon Profil', href: '/profile', icon: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>' }
		],
		TEACHER: [
			{ name: 'Dashboard', href: '/teacher', icon: '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>' },
			{ name: 'Copies à corriger', href: '/teacher/submissions', icon: '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"/><path d="M5.45 5.11L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>' },
			{ name: 'Suivi des Élèves', href: '/teacher/students', icon: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>' },
			{ name: 'Consulter le Cursus', href: '/teacher/cursus', icon: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>' }
		],
		ADMIN: [
			{ name: 'Vue Générale', href: '/admin', icon: '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>' },
			{ name: 'Gestion du Cursus', href: '/admin/cursus', icon: '<path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.93a2 2 0 0 1-1.66-.9l-.82-1.2A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13c0 1.1.9 2 2 2Z"/><path d="M14 13h3"/><path d="M14 17h3"/><path d="M10 9v8"/>' },
			{ name: 'Gestion des Comptes', href: '/admin/users', icon: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v4"/><path d="M12 16h.01"/>' },
			{ name: 'Configuration', href: '/admin/settings', icon: '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>' }
		]
	};

	let currentMenu = $derived(user && menus[user.role] ? menus[user.role] : []);
</script>

{#if loading}
	<div class="flex h-screen w-full items-center justify-center bg-base-200">
		<span class="loading loading-spinner loading-lg text-primary"></span>
	</div>
{:else if user}
	<div class="h-screen w-full bg-base-200 p-4 md:p-6 font-sans text-base-content overflow-hidden flex gap-4 md:gap-6">
		
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
					{#each currentMenu as item}
						<li class="relative">
							{#if $page.url.pathname === item.href || $page.url.pathname.startsWith(item.href + '/')}
								<div class="absolute -left-6 top-0 bottom-0 w-1.5 rounded-r-lg bg-primary"></div>
								<a href={item.href} class="flex gap-3 bg-transparent hover:bg-base-200 text-primary font-bold active:bg-base-200">
									<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
										{@html item.icon}
									</svg>
									{item.name}
								</a>
							{:else}
								<a href={item.href} class="flex gap-3 text-base-content/70 hover:text-base-content">
									<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
										{@html item.icon}
									</svg>
									{item.name}
								</a>
							{/if}
						</li>
					{/each}
				</ul>
			</div>

			<!-- GENERAL Section -->
			<div class="mt-auto px-6 pt-4">
				<div class="mb-4 text-xs font-bold tracking-wider text-base-content/50 uppercase">General</div>
				<ul class="menu menu-md p-0 space-y-2">
					<li>
						<a href="/dashboard/settings" class="flex gap-3 text-base-content/70 hover:text-base-content">
							<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
								<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>
							</svg>
							Settings
						</a>
					</li>
					<li>
						<a href="/dashboard/help" class="flex gap-3 text-base-content/70 hover:text-base-content">
							<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
								<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>
							</svg>
							Help
						</a>
					</li>
					<li>
						<a href="/auth/login" class="flex gap-3 text-base-content/70 hover:text-error hover:bg-error/10" onclick={() => { localStorage.clear(); }}>
							<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
								<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/>
							</svg>
							Logout
						</a>
					</li>
				</ul>
			</div>
		</aside>

		<div class="flex flex-1 flex-col gap-4 md:gap-6 overflow-hidden">
			<header class="flex h-[88px] shrink-0 items-center justify-between rounded-[2rem] bg-base-100 px-6 md:px-10 shadow-sm">
				
				<div class="md:hidden flex-none">
					<button class="btn btn-square btn-ghost">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-6 h-6 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
					</button>
				</div>

				<div class="relative w-full max-w-md hidden sm:block">
					<svg xmlns="http://www.w3.org/2000/svg" class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-base-content/40" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
						<path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
					</svg>
					<input type="text" placeholder="Search task" class="input bg-base-200/50 w-full rounded-2xl pl-12 pr-14 focus:bg-base-200 transition-colors border-none outline-none" />
					<div class="absolute right-3 top-1/2 -translate-y-1/2 rounded-lg bg-base-100 px-2 py-1 text-xs font-bold text-base-content/40 shadow-sm border border-base-200">
						⌘F
					</div>
				</div>

				<div class="flex items-center gap-2 md:gap-6 ml-auto">
					<button class="btn btn-circle btn-ghost text-base-content/60">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
						</svg>
					</button>

					<button class="btn btn-circle btn-ghost text-base-content/60 relative">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
						</svg>
						<span class="absolute right-2 top-2 h-2.5 w-2.5 rounded-full bg-error border-2 border-base-100"></span>
					</button>

					<div class="dropdown dropdown-end">
						<button tabindex="0" class="flex items-center gap-3 pl-2 btn btn-ghost h-auto hover:bg-transparent px-2">
							<div class="avatar">
								<div class="w-10 rounded-full border-2 border-base-100 shadow-sm flex items-center justify-center bg-primary text-primary-content font-bold">
									{user.first_name?.[0] || 'U'}{user.last_name?.[0] || ''}
								</div>
							</div>
							<div class="hidden text-left sm:block">
								<div class="text-sm font-bold text-base-content">{user.first_name} {user.last_name}</div>
								<div class="text-[10px] font-bold text-primary uppercase">{user.role}</div>
								<div class="text-xs font-medium text-base-content/50">{user.email}</div>
							</div>
						</button>
						<ul tabindex="0" class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52 z-[1] mt-4 border border-base-200">
							<li><a>Profil</a></li>
							<li><a>Paramètres</a></li>
							<li class="text-error"><a href="/auth/login" onclick={() => { localStorage.clear(); }}>Déconnexion</a></li>
						</ul>
					</div>
				</div>
			</header>

			<main class="flex-1 overflow-y-auto rounded-[2rem] bg-base-100 p-6 md:p-10 shadow-sm no-scrollbar">
				{@render children()}
			</main>
		</div>
	</div>
{/if}

<style>
	.no-scrollbar::-webkit-scrollbar { display: none; }
	.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>
