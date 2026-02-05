import mParticle from '@mparticle/web-sdk';
import '@mparticle/web-google-analytics-4-server-kit';

let mParticleConfig = {
   isDevelopmentMode: false,
}

mParticle.init("eu1-5968b18e4b7eff49b601e8bc86b0707e", mParticleConfig);

mParticle.logPageView(
	"experiment_screen_view",
	{page: window.location.toString()},
	{"Google.Page": window.location.pathname.toString()}
);

