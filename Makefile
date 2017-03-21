REPO = repo
ARGS = "--user"
LIRI_SDK_VERSION = "master"
GPGKEY = "71B9937D"

all: $(REPO)/config $(foreach file, $(wildcard io.liri.*.json), $(subst .json,.app,$(file)))

$(REPO)/config:
	ostree init --mode=archive-z2 --repo=$(REPO)

%.app: %.json
	flatpak-builder --force-clean --ccache --repo=$(REPO) --subject="Build of $<, `date`" --gpg-sign=$(GPGKEY) ${EXPORT_ARGS} app $<

export:
	flatpak build-update-repo --prune --prune-depth=20 $(REPO) --gpg-sign=$(GPGKEY) ${EXPORT_ARGS}

remotes:
	flatpak remote-add $(ARGS) liri --from https://files.liri.io/flatpak/liri.flatpakrepo --if-not-exists

deps:
	flatpak install $(ARGS) liri io.liri.Platform $(LIRI_SDK_VERSION); true
	flatpak install $(ARGS) liri io.liri.Sdk $(LIRI_SDK_VERSION); true

update-deps:
	flatpak update $(ARGS) --runtime io.liri.Platform $(LIRI_SDK_VERSION); true
	flatpak update $(ARGS) --runtime io.liri.Sdk $(LIRI_SDK_VERSION); true

check:
	@json-glib-validate *.json

clean:
	@rm -rf $(TMP) .flatpak-builder
