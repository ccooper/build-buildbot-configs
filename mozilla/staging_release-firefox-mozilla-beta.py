# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
EMAIL_RECIPIENTS = []

releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True
releaseConfig['base_clobber_url'] = 'https://api-pub-build.allizom.org/clobberer/forceclobber'

# Release Notification
releaseConfig['AllRecipients']       = EMAIL_RECIPIENTS
releaseConfig['ImportantRecipients'] = EMAIL_RECIPIENTS
releaseConfig['AVVendorsRecipients'] = EMAIL_RECIPIENTS
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[staging-release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['stage_product']       = 'firefox'
releaseConfig['appName']             = 'browser'
#  Current version info
releaseConfig['version']             = '33.0b3'
releaseConfig['appVersion']          = '33.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_33_0b3'
releaseConfig['partialUpdates']      = {

    '33.0b2': {
        'appVersion': '33.0',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_33_0b2',
    },

}
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-beta',
        'path': 'users/stage-ffxbld/mozilla-beta',
        'revision': 'default',
        'relbranch': None,
        'bumpFiles': {
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-beta'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_AUTOMATION',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/mozharness': 'production',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = True

# Mercurial account
releaseConfig['hgUsername']          = 'stage-ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_rsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['stagingServer']       = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['previousReleasesStagingServer'] = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'http://dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausHost']             = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausUser']             = 'ffxbld'
releaseConfig['ausSshKey']           = 'ffxbld_rsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['updateVerifyChunks']  = 6
releaseConfig['mozconfigs']          = {
    'linux': 'browser/config/mozconfigs/linux32/beta',
    'linux64': 'browser/config/mozconfigs/linux64/beta',
    'macosx64': 'browser/config/mozconfigs/macosx-universal/beta',
    'win32': 'browser/config/mozconfigs/win32/beta',
}
releaseConfig['xulrunner_mozconfigs']          = {
    'linux': 'xulrunner/config/mozconfigs/linux32/xulrunner',
    'linux64': 'xulrunner/config/mozconfigs/linux64/xulrunner',
    'macosx64': 'xulrunner/config/mozconfigs/macosx-universal/xulrunner',
    'win32': 'xulrunner/config/mozconfigs/win32/xulrunner',
}
releaseConfig['releaseChannel']        = 'beta'
releaseConfig['updateChannels'] = {
    "beta": {
        "versionRegex": r"^.*$",
        "ruleId": 26,
        "patcherConfig": "mozBeta-branch-patcher2.cfg",
        "localTestChannel": "beta-localtest",
        "cdnTestChannel": "beta-cdntest",
        "verifyConfigs": {
            "linux":  "mozBeta-firefox-linux.cfg",
            "linux64":  "mozBeta-firefox-linux64.cfg",
            "macosx64": "mozBeta-firefox-mac64.cfg",
            "win32":  "mozBeta-firefox-win32.cfg",
            "win64":  "mozBeta-firefox-win32.cfg",
        },
        "testChannels": {
            "beta-cdntest": {
                "ruleId": 41,
            },
            "beta-localtest": {
                "ruleId": 40,
            },
        }
    }
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'users/stage-ffxbld/partner-repacks'

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.allizom.org/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_firefox_beta.py'

# Misc configuration
releaseConfig['build_tools_repo_path'] = "users/stage-ffxbld/tools"
releaseConfig['enableAutomaticPushToMirrors'] = True
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['ftpSymlinkName'] = 'latest-beta'
releaseConfig['bouncer_aliases'] = {
    'Firefox-%(version)s': 'firefox-beta-latest',
    'Firefox-%(version)s-stub': 'firefox-beta-stub',
}
