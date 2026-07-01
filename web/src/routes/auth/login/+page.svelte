<script>
    import { goto } from '$app/navigation';
    import api from '$lib/index.js';
    import { ACCESS_TOKEN, REFRESH_TOKEN } from '$lib/constants.js';

    let email = $state('');
    let password = $state('');
    let error = $state('');
    let loading = $state(false);

    async function handleLogin(e) {
        e.preventDefault();
        error = '';
        loading = true;
        try {
            const res = await api.post('api/token/', { email, password });
            localStorage.setItem(ACCESS_TOKEN, res.data.access);
            localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
            goto('/dashboard/student/');
        } catch (err) {
            error = "Email ou mot de passe incorrect.";
            console.error(err);
        } finally {
            loading = false;
        }
    }
</script>

<div class="min-h-screen flex items-center justify-center bg-base-200 p-4">
    <div class="card w-full max-w-md bg-base-100 shadow-xl">
        <div class="card-body">
            <h2 class="card-title text-2xl font-bold justify-center mb-6">Connexion</h2>
            
            {#if error}
                <div class="alert alert-error text-sm mb-4">
                    <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    <span>{error}</span>
                </div>
            {/if}

            <form onsubmit={handleLogin}>
                <div class="form-control w-full mb-4">
                    <label class="label">
                        <span class="label-text">Adresse email</span>
                    </label>
                    <input type="email" bind:value={email} required class="input input-bordered w-full" placeholder="exemple@domaine.com" />
                </div>
                
                <div class="form-control w-full mb-6">
                    <label class="label">
                        <span class="label-text">Mot de passe</span>
                    </label>
                    <input type="password" bind:value={password} required class="input input-bordered w-full" placeholder="••••••••" />
                </div>

                <button type="submit" class="btn btn-primary w-full" disabled={loading}>
                    {#if loading}
                        <span class="loading loading-spinner"></span>
                    {/if}
                    Se connecter
                </button>
            </form>
            
            <div class="divider">OU</div>
            
            <div class="text-center mt-4">
                <p class="text-sm">Pas encore de compte ? <a href="/auth/register" class="link link-primary">S'inscrire</a></p>
            </div>
        </div>
    </div>
</div>
