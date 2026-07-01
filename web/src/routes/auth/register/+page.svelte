<script>
    import { goto } from '$app/navigation';
    import api from '$lib/index.js';

    let first_name = $state('');
    let last_name = $state('');
    let email = $state('');
    let password = $state('');
    let error = $state('');
    let success = $state('');
    let loading = $state(false);

    async function handleRegister(e) {
        e.preventDefault();
        error = '';
        success = '';
        loading = true;
        try {
            // Le backend va générer le username automatiquement à partir de first_name et last_name
            await api.post('api/user/register/', { 
                first_name, 
                last_name, 
                email, 
                password,
                username: email // On passe l'email comme username par défaut pour passer la validation du serializer si besoin
            });
            success = "Compte créé avec succès ! Redirection vers la page de connexion...";
            setTimeout(() => {
                goto('/auth/login');
            }, 2000);
        } catch (err) {
            error = err.response?.data?.detail || "Une erreur s'est produite lors de l'inscription.";
            if (err.response?.data && typeof err.response.data === 'object' && !err.response.data.detail) {
                const fields = Object.keys(err.response.data);
                if (fields.length > 0) {
                    const fieldError = Array.isArray(err.response.data[fields[0]]) 
                        ? err.response.data[fields[0]][0] 
                        : err.response.data[fields[0]];
                    error = `${fields[0]}: ${fieldError}`;
                }
            }
            console.error(err);
        } finally {
            loading = false;
        }
    }
</script>

<div class="min-h-screen flex items-center justify-center bg-base-200 p-4">
    <div class="card w-full max-w-md bg-base-100 shadow-xl">
        <div class="card-body">
            <h2 class="card-title text-2xl font-bold justify-center mb-6">Inscription</h2>
            
            {#if error}
                <div class="alert alert-error text-sm mb-4">
                    <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    <span>{error}</span>
                </div>
            {/if}

            {#if success}
                <div class="alert alert-success text-sm mb-4">
                    <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    <span>{success}</span>
                </div>
            {/if}

            <form onsubmit={handleRegister}>
                <div class="flex gap-4 mb-4">
                    <div class="form-control w-1/2">
                        <label class="label">
                            <span class="label-text">Prénom</span>
                        </label>
                        <input type="text" bind:value={first_name} required class="input input-bordered w-full" placeholder="Prénom" />
                    </div>
                    <div class="form-control w-1/2">
                        <label class="label">
                            <span class="label-text">Nom</span>
                        </label>
                        <input type="text" bind:value={last_name} required class="input input-bordered w-full" placeholder="Nom" />
                    </div>
                </div>

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
                    <input type="password" bind:value={password} required class="input input-bordered w-full" placeholder="••••••••" minlength="8" />
                </div>

                <button type="submit" class="btn btn-primary w-full" disabled={loading}>
                    {#if loading}
                        <span class="loading loading-spinner"></span>
                    {/if}
                    S'inscrire
                </button>
            </form>
            
            <div class="divider">OU</div>
            
            <div class="text-center mt-4">
                <p class="text-sm">Déjà un compte ? <a href="/auth/login" class="link link-primary">Se connecter</a></p>
            </div>
        </div>
    </div>
</div>
