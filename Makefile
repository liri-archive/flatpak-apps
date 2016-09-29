#all: io.liri.Settings.app
all: io.liri.Terminal.app io.liri.Photos.app io.github.communi.app

%.app: %.json
	rm -rf app
	xdg-app-builder --ccache --require-changes --repo=repo --subject="Build of $<, `date`" ${EXPORT_ARGS} app $<

update-repo:
	xdg-app build-update-repo --prune --prune-depth=20  ${EXPORT_ARGS-} repo
