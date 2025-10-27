class User < ApplicationRecord
    has_secure_password
    validates :password, presence: true
    validates :email, presence: true, uniqueness: true
    validates :username, presence: true, uniqueness: true
    normalizes :email, with: ->(email) { email.strip.downcase }
end
